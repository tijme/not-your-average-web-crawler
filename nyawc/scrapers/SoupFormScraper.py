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
from nyawc.helpers.URLHelper import URLHelper
from bs4 import BeautifulSoup
from collections import OrderedDict

import html5lib

class SoupFormScraper:
    """The SoupLinkScraper finds requests from forms in HTML using BeautifulSoup.

    Attributes:
        content_types list(str): The supported content types.
        __queue_item (obj): The queue item containing the response to scrape.

    """

    content_types = [
        "text/html"
    ]

    __queue_item = None

    def __init__(self, queue_item):
        """Construct the SoupFormScraper class.

        Args:
            queue_item (obj): The queue item containing a response the scrape.

        """

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

        url = URLHelper.make_absolute(host, self.__trim_grave_accent(soup['action'])) if soup.has_attr('action') else host
        method_original = soup['method'] if soup.has_attr('method') else 'get'
        method = 'post' if method_original.lower() == 'post' else 'get'
        data = self.__get_form_data(soup)

        return Request(url, method, data)


    def __trim_grave_accent(self, href):
        """Trim grave accents manually (because BeautifulSoup doesn't support it).

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

        fields = OrderedDict()

        self.__get_form_data_from_inputs(soup, fields)
        self.__get_form_data_from_buttons(soup, fields)
        self.__get_form_data_from_textareas(soup, fields)
        self.__get_form_data_from_selects(soup, fields)

        return fields

    def __get_form_data_from_inputs(self, soup, fields):
        """Parse all the form data from input elements

        Args:
            soup (obj): The BeautifulSoup form.
            fields (obj): The fields (key/value) OrderedDict.

        """

        for input in soup.find_all('input'):
            if not input.has_attr('name'):
                continue
            
            if input['type'] in ('text', 'hidden', 'email', 'password', 'submit', 'image', 'color', 'date', 'month', 'number', 'search', 'tel', 'time', 'url', 'week', 'range'):
                fields[input['name']] = input['value'] if input.has_attr('value') else ''
                continue
            
            if input['type'] in ('checkbox', 'radio'):
                value = ''

                if input.has_attr('checked'):
                    if input.has_attr('value'):
                        value = input['value']
                    else:
                        value = 'on'

                if input['name'] in fields and value:
                    fields[input['name']] = value
                
                if not input['name'] in fields:
                    fields[input['name']] = value
                
                continue

    def __get_form_data_from_buttons(self, soup, fields):
        """Parse all the form data from button elements

        Args:
            soup (obj): The BeautifulSoup form.
            fields (obj): The fields (key/value) dict.

        """

        for button in soup.find_all('button'):
            if not button.has_attr('name'):
                continue

            fields[button['name']] = button['value'] if button.has_attr('value') else ''

    def __get_form_data_from_textareas(self, soup, fields):
        """Parse all the form data from textarea elements

        Args:
            soup (obj): The BeautifulSoup form.
            fields (obj): The fields (key/value) dict.

        """

        for textarea in soup.find_all('textarea'):
            if not textarea.has_attr('name'):
                continue

            fields[textarea['name']] = textarea.string or ''

    def __get_form_data_from_selects(self, soup, fields):
        """Parse all the form data from select elements

        Args:
            soup (obj): The BeautifulSoup form.
            fields (obj): The fields (key/value) dict.

        """

        for select in soup.find_all('select'):
            if not select.has_attr('name'):
                continue

            value = ''

            options = select.find_all('option')
            is_multiple = select.has_attr('multiple')

            selected_options = [
                option for option in options
                if option.has_attr('selected')
            ]
            
            if not selected_options and options:
                selected_options = [options[0]]
            
            if not is_multiple:
                if len(selected_options) >= 1:
                    value = selected_options[0]['value']
            else:
                value = [option['value'] for option in selected_options]
            
            fields[select['name']] = value