#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html
import gzip
import json
from urllib.request import Request, urlopen


def search(keywords):
    """
    stackoverflow search
    :param keywords:     ['linux']
    :return:
    """
    limit = 10
    if not isinstance(keywords, list) or not keywords:
        return []
    url = 'https://api.stackexchange.com/2.2/search/advanced?site=stackoverflow&pagesize={}&order=desc&sort=votes&q={}&filter=default'.format(
        limit, '+'.join(keywords))
    request = Request(url)
    request.add_header("User-Agent",
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0')

    html_source = gzip.decompress(urlopen(request).read()).decode('utf-8')
    d = json.loads(html_source)

    def _reputation(i):
        return 'Vote {} Tag {} Answer {}'.format(i['score'], ' '.join(i['tags'][:3]), i['answer_count'])

    return [{'title': html.unescape(i['title']), 'subtitle': _reputation(i), 'icon': './stackoverflow/logo.png',
             'link': i['link']} for
            i in d['items']]
