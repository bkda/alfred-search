#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import match
from urllib.parse import unquote
from urllib.parse import urlencode
from html.parser import HTMLParser
from base import Base


class GoogleParser(HTMLParser):
    h3_flag = False
    a_flag = False
    b_flag = False
    title_part = ''

    def __init__(self):
        HTMLParser.__init__(self)
        self.result_info = []
        self.link = ''
        self.title = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs == [('class', 'r')]:
            self.h3_flag = True

        if tag == 'a' and self.h3_flag:
            self.a_flag = True

        if tag == 'b' and self.a_flag:
            self.b_flag = True

        if self.a_flag:
            for (key, value) in attrs:
                if key == 'href':
                    if value.startswith("/url?"):
                        m = match('/url\?(url|q)=(.+?)&', value)
                        if m and len(m.groups()) == 2:
                            href = unquote(m.group(2))
                            self.link = href
                    else:
                        self.link = value

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.h3_flag = False
        if tag == 'a' and self.a_flag:
            self.a_flag = False
            self.result_info.append({
                'title': self.title_part,
                'link': self.link,
                'subtitle': self.link,
                'icon': './google/logo.png'
            })
            self.title_part = ''

    def handle_data(self, data):
        if self.a_flag:
            self.title_part += data


class Google(Base):
    def prepare(self):
        self.url = "http://www.google.com/search?" + urlencode({'q': self.query}) + u"&pws=0&gl=us&gws_rd=cr"

    def parser(self):
        google_parser = GoogleParser()
        google_parser.feed(self.data)
        google_parser.close()
        return google_parser.result_info
