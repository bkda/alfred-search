#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from xml.etree.ElementTree import Element, SubElement, tostring

import zhihu
import wolframalpha


def convert_list_to_xml(result_list, _type):
    """
    convert list to xml
    :param result_list:
    :param _type:
    :return:
    """
    items = Element("items")
    for result in result_list:
        item = SubElement(items, "item", attrib={"arg": result['link']})
        title = SubElement(item, "title")
        subtitle = SubElement(item, "subtitle")
        icon = SubElement(item, "icon")

        title.text = result['title']
        subtitle.text = result['subtitle']
        icon.text = result['icon']
    return tostring(items, encoding='unicode')


def unknown_search_engine():
    return raise_error()


def raise_error(error):
    if not isinstance(error, str):
        error = 'Unknown search engine'
    return [{'title': 'Error', 'subtitle': error, 'icon': 'error.png', 'quicklookurl': ''}]


if __name__ == '__main__':
    fd = {
        'zhihu': zhihu.search,
        'wolframalpha':wolframalpha.search
    }
    data = fd.get(sys.argv[1], raise_error)(sys.argv[2:])
    xml = convert_list_to_xml(result_list=data, _type=sys.argv[1])
    sys.stdout.write(xml)
