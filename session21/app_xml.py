from xml.dom.minidom import parseString, parse

xml = """<?xml version="1.0" encoding="UTF-8"?>
<library>
 <book>
   <title>The Great Gatsby</title>
   <author>F. Scott Fitzgerald</author>
   <year>1925</year>
 </book>
</library>
"""

documento = parseString(xml)

print(documento.getElementsByTagName('title')[0].firstChild.nodeValue)

documento = parse('./sample.xml')

print(documento.getElementByTagName('item')[0].firstChild.nodeValue)

import xml.etree.ElementTree as ET

root = ET.parse('./sample.xml')

parse_dict = dict()

for child in root.iter():
    if child.text.strip():
        parse_dict[child.tag] = child.text

print(parse_dict)