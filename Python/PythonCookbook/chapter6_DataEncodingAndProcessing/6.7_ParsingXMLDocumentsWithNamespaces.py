from xml.etree.ElementTree import parse

file = open('test.xml')
doc = parse(file)
print(doc.findtext('author'))
print(doc.find('content'))
print(doc.find('content/html'))
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
