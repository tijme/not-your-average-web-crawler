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

from src.http.Request import Request
from src.helpers.URLHelper import URLHelper
from bs4 import BeautifulSoup
import html5lib
import sys

class SoupFormScraper:

    content_types = [
        "text/html"
    ]

    __queue_item = None

    def __init__(self, queue_item):
        self.__queue_item = queue_item

    def get_requests(self):
        soup = BeautifulSoup(self.__queue_item.response.text, "html5lib")
        forms = soup.find_all("form")

        found_requests = []

        for form in forms:
            found_requests.append(self.__get_request(form))

        return found_requests

    def __get_request(self, form):
        host = self.__queue_item.request.url
        url = URLHelper.make_absolute(host, self.__trim_grave_accent(form['action'])) if form.has_attr('action') else host
        method_original = form['method'] if form.has_attr('method') else 'get'
        method = 'post' if method_original.lower() == 'post' else 'get'
        data = self.__get_form_data(form)

        return Request(url, method, data)


    def __trim_grave_accent(self, href):
        if href.startswith("`"):
            href = href[1:]

        if href.endswith("`"):
            href = href[:-1]

        return href

    def __get_form_data(self, soup):
        "Turn a BeautifulSoup form in to a dict of fields and default values"
        fields = {}

        for input in soup.findAll('input'):
            # ignore if no name attribute
            if not input.has_attr('name'):
                continue
            
            # single element nome/value fields
            if input['type'] in ('text', 'hidden', 'email', 'password', 'submit', 'image'):
                value = ''
                if input.has_attr('value'):
                    value = input['value']
                fields[input['name']] = value
                continue
            
            # checkboxes and radios
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
            
            assert False, 'input type %s not supported' % input['type']
        
        # textareas
        for textarea in soup.findAll('textarea'):
            # ignore if no name attribute
            if not textarea.has_attr('name'):
                continue

            fields[textarea['name']] = textarea.string or ''
        
        # select fields
        for select in soup.findAll('select'):
            # ignore if no name attribute
            if not select.has_attr('name'):
                continue

            value = ''
            options = select.findAll('option')
            is_multiple = select.has_attr('multiple')
            selected_options = [
                option for option in options
                if option.has_attr('selected')
            ]
            
            # If no select options, go with the first one
            if not selected_options and options:
                selected_options = [options[0]]
            
            if not is_multiple:
                assert(len(selected_options) < 2)
                if len(selected_options) == 1:
                    value = selected_options[0]['value']
            else:
                value = [option['value'] for option in selected_options]
            
            fields[select['name']] = value
        
        return fields