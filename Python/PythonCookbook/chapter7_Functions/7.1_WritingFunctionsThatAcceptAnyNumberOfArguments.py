def avg(first, *rest):
    return (first + sum(rest) / (1 + len(rest)))


print(avg(1, 2))
print(avg(1, 2, 3, 4, 5, 6))

print("-------------------")
import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'

result = make_element('item', 'Albatross', size='large', quantity=6)
# Creates '<p>&lt;spam&gt;</p>'
result2 = make_element('p', '<spam>')

print(result)
print(result2)
