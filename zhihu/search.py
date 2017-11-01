#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import urlencode


def search(keywords):
    """
    zhihu search
    :param keywords:     ['linux']
    :return:
    """
    tag_dict = {'topic': '话题 {}个精选回答', 'people': '用户 {}', 'question': '问题 {}个回答', 'article': '文章 {}个赞'}
    icon_dict = {
        'topic': './zhihu/logo.png',
        'question': './zhihu/logo.png',
        'article': './zhihu/zhuanlan.png'
    }
    link_dict = {'article': 'https://zhuanlan.zhihu.com/p/{}'}
    if not isinstance(keywords, list) or not keywords:
        return []
    url = 'https://www.zhihu.com/autocomplete?{}'.format(urlencode({'token': ' '.join(keywords)}))

    request = Request(url)
    request.add_header("User-Agent",
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0')
    html_source = urlopen(request).read()

    def _download_avatar(d):
        try:
            img_path = './zhihu/user_avatar/{}.jpg'.format(d[2])
            if not os.path.exists(img_path):
                img_path, _ = urlretrieve(d[3].replace('_s', '_m'), img_path)
            return img_path
        except Exception:
            return './zhihu/logo.png'

    def _logo(d):
        return icon_dict.get(d[0], _download_avatar(d))

    def _subtitle(d):
        return tag_dict.get(d[0], '{}').format(d[-3] or d[-2])

    def _link(d):
        return link_dict.get(d[0], 'https://www.zhihu.com/%s/{}' % d[0]).format(d[2] or d[3])

    return [{'title': i[1], 'subtitle': _subtitle(i), 'icon': _logo(i), 'link': _link(i)} for i in
            json.loads(html_source)[0][1:-1]]
