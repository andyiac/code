import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
print(u)


f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
# print(text)

import sys


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')

print(sys.stdout.encoding)
