from collections import Counter
from xml.etree.ElementTree import parse, iterparse

potholes_by_zip = Counter()


# in memory methods
# doc = parse('/Users/andyiac/Downloads/potholes.xml')
# for pothole in doc.iterfind('row/row'):
#     potholes_by_zip[pothole.findtext('zip')] += 1
#
# for zipcode, num in potholes_by_zip.most_common():
#     print(zipcode, num)


def prase_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


data = prase_and_remove('/Users/andyiac/Downloads/potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
