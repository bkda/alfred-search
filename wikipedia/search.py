#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import Base


class Wikipedia(Base):
    def prepare(self):
        self.url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit={}&format=json'.format(
            ' '.join(self.query), self.limit)

    def parser(self):
        return [{'title': self.data[1][i], 'subtitle': self.data[2][i], 'icon': './wikipedia/logo.png',
                 'link': self.data[3][i]} for i in range(self.limit)]
