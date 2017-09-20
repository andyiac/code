import json

data = {
    'name': 'ACME',
    'share': 100,
    'price': 542.23,
}

print(data)

json_str = json.dumps(data)

print(json_str)

print(json.loads(json_str))

print("-----------------")

from urllib.request import urlopen
import json

u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint

pprint(resp)
