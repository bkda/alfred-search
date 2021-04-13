#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import json
from collections import namedtuple
from urllib.request import Request, urlopen, build_opener
from PySocks import socks
from PySocks.sockshandler import SocksiPyHandler

Proxy = namedtuple('Proxy', 'host port')


class Base:
    def __init__(self, query):
        self.query = query
        self.limit = 10
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
        self.url = None
        self.proxy = None
        self.data = None
        self.prepare()
        self.process_request()

    def process_request(self):
        """
        :return:
        """
        if self.proxy is not None:
            host, port = self.proxy
            handler = SocksiPyHandler(socks.SOCKS5, host, port)
            opener = build_opener(handler)
            opener.addheaders = [('User-agent', self.ua)]
            res = opener.open(self.url)
            html_source = res.read()
        else:
            res = Request(self.url)
            res.add_header("User-Agent", self.ua)
            res = urlopen(res)
            html_source = res.read()
            if res.headers.get('Content-Encoding') == 'gzip':
                html_source = gzip.decompress(html_source)
            self.data = html_source.decode('utf-8')
            if 'application/json' in res.headers.get('Content-Type').lower():
                self.data = json.loads(self.data)

    def prepare(self):
        pass

    def parser(self):
        pass
