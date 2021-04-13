#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from base import Base


class Wolframalpha(Base):
    def prepare(self):
        self.url = 'https://www.wolframalpha.com/input/autocomplete.jsp?{}'.format(
            urlencode({'i': ' '.join(self.query)}))

    def parser(self):
        return [{'title': i['input'], 'subtitle': i.get('description'), 'icon': './wolframalpha/logo.png',
                 'link': 'https://www.wolframalpha.com' + i['waPath']} for i in self.data['results']]
