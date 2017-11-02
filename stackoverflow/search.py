#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html
from base import Base


class Stackoverflow(Base):
    def prepare(self):
        self.url = 'https://api.stackexchange.com/2.2/search/advanced?site=stackoverflow&pagesize={}&order=desc&sort=votes&q={}&filter=default'.format(
            self.limit, '+'.join(self.query))

    def parser(self):
        def _reputation(i):
            return 'Vote {} Tag {} Answer {}'.format(i['score'], ' '.join(i['tags'][:3]), i['answer_count'])

        return [{'title': html.unescape(i['title']), 'subtitle': _reputation(i), 'icon': './stackoverflow/logo.png',
                 'link': i['link']} for i in self.data['items']]
