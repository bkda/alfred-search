#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from xml.etree.ElementTree import Element, SubElement, tostring

from zhihu import Zhihu
from wolframalpha import Wolframalpha
from wikipedia import Wikipedia
from stackoverflow import Stackoverflow
from google import Google


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


if __name__ == '__main__':
    fd = {
        'zhihu': Zhihu,
        'wolframalpha': Wolframalpha,
        'wikipedia': Wikipedia,
        'stackoverflow': Stackoverflow,
        'google': Google
    }
    r = fd.get(sys.argv[1])(sys.argv[2:])
    xml = convert_list_to_xml(result_list=r.parser(), _type=sys.argv[1])
    sys.stdout.write(xml)
