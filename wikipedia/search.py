#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib.request import Request, urlopen


def search(keywords):
    """
    wikipedia search
    :param keywords:     ['linux']
    :return:
    """
    limit = 10
    if not isinstance(keywords, list) or not keywords:
        return []
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit={}&format=json'.format(
        ' '.join(keywords), limit)

    request = Request(url)
    request.add_header("User-Agent",
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0')
    html_source = urlopen(request).read()
    d = json.loads(html_source)
    return [{'title': d[1][i], 'subtitle': d[2][i], 'icon': './wikipedia/logo.png', 'link': d[3][i]} for i in
            range(limit)]
