#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def search(keywords):
    """
    wolframalpha search
    :param keywords:     ['linux']
    :return:
    """
    if not isinstance(keywords, list) or not keywords:
        return []
    url = 'https://www.wolframalpha.com/input/autocomplete.jsp?{}'.format(urlencode({'i': ' '.join(keywords)}))

    request = Request(url)
    request.add_header("User-Agent",
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0')
    html_source = urlopen(request).read()

    return [
        {'title': i['input'], 'subtitle': i['description'], 'icon': './wolframalpha/logo.png',
         'link': 'https://www.wolframalpha.com' + i['waPath']} for i in json.loads(html_source)['results']]
