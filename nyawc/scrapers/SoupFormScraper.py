# -*- coding: utf-8 -*-

# MIT License
# 
# Copyright (c) 2017 Tijme Gommers
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from nyawc.http.Request import Request
from nyawc.Crawler import CrawlerActions
from nyawc.helpers.URLHelper import URLHelper
from nyawc.helpers.RandomInputHelper import RandomInputHelper
from bs4 import BeautifulSoup
from collections import OrderedDict

import html5lib

class SoupFormScraper:
    """The SoupLinkScraper finds requests from forms in HTML using BeautifulSoup.

    Attributes:
        content_types list(str): The supported content types.
        __options (obj): The settins/options object.
        __queue_item (obj): The queue item containing the response to scrape.

    """

    content_types = [
        "text/html"
    ]

    __options = None

    __queue_item = None

    def __init__(self, options, queue_item):
        """Construct the SoupFormScraper class.

        Args:
            options (obj): The settins/options object.
            queue_item (obj): The queue item containing a response the scrape.

        """

        self.__options = options
        self.__queue_item = queue_item

    def get_requests(self):
        """Get all the new requests that were found in the response.

        Returns:
            list(obj): A list of new requests.

        """

        host = self.__queue_item.request.url
        content = self.__queue_item.response.text

        return self.get_requests_from_content(host, content)

    def get_requests_from_content(self, host, content):
        """Find new requests from the given content.

        Args:
            host (str): The parent request URL.
            content (obj): The HTML content.

        Returns:
            list(obj): Requests that were found.

        """

        soup = BeautifulSoup(content, "html5lib")
        forms = soup.find_all("form")

        found_requests = []

        for form in forms:
            found_requests.append(self.__get_request(host, form))

        return found_requests

    def __get_request(self, host, soup):
        """Build a request from the given soup form.

        Args:
            host str: The URL of the current queue item.
            soup (obj): The BeautifulSoup form.

        Returns:
            obj: The new Request.

        """

        url = URLHelper.make_absolute(host, self.__trim_grave_accent(soup["action"])) if soup.has_attr("action") else host
        method_original = soup["method"] if soup.has_attr("method") else "get"
        method = "post" if method_original.lower() == "post" else "get"
        data = self.__get_form_data(soup)

        return Request(url, method, data)


    def __trim_grave_accent(self, href):
        """Trim grave accents manually (because BeautifulSoup doesn"t support it).

        Args:
            href (str): The BeautifulSoup href value.

        Returns:
            str: The BeautifulSoup href value without grave accents.

        """

        if href.startswith("`"):
            href = href[1:]

        if href.endswith("`"):
            href = href[:-1]

        return href

    def __get_form_data(self, soup):
        """Build a form data dict from the given form.

        Args:
            soup (obj): The BeautifulSoup form.

        Returns:
            obj: The form data (key/value).

        """

        elements = self.__get_all_valid_form_data_elements(soup)
        form_data = OrderedDict()

        for element in elements:
            default_value = self.__get_default_value_from_element(element)
            if default_value is not False:
                form_data[element["name"]] = default_value

        action = self.__options.callbacks.form_before_autofill(self.__queue_item, elements, form_data)

        if action == CrawlerActions.DO_NOT_AUTOFILL_FORM:
            return form_data

        for element in elements:
            if not hasattr(form_data, element["name"]) and element.has_attr("type"):
                form_data[element["name"]] = RandomInputHelper.get_for_type(element["type"])

        return form_data

    def __get_all_valid_form_data_elements(self, soup):
        elements = []

        for element in soup.find_all(["input", "button", "textarea", "select"]):
            if element.has_attr("name"):
                elements.append(element)

        return elements

    def __get_default_value_from_element(self, element):

        if element.name == "select":
            options = element.find_all("option")
            is_multiple = element.has_attr("multiple")

            selected_options = [
                option for option in options
                if option.has_attr("selected")
            ]
            
            if not selected_options and options:
                selected_options = [options[0]]
            
            if not is_multiple:
                if len(selected_options) >= 1:
                    if selected_options[0].has_attr("value"):
                        return selected_options[0]["value"]
                    else:
                        return selected_options[0].string
            else:
                return [option["value"] if option.has_attr("value") else option.string for option in selected_options]
            
        if element.name == "textarea":
            return element.string if element.string is not None else ""

        if element.name == "input" and element.has_attr("type"):
            if element["type"] in ("checkbox", "radio"):
                if not element.has_attr("checked"):
                    return False

                if element.has_attr("value"):
                    return element["value"]
                else:
                    return "on"

        if element.has_attr("value"):
            return element["value"]

        return ""