s = b'hello'
import base64

a = base64.b64encode(s)
print(a)

b = base64.b64decode(a)

print(b)
