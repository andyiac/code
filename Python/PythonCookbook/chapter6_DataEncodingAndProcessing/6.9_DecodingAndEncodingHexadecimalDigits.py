s = b'hello'

import binascii

h = binascii.b2a_hex(s)
print(h)

print(binascii.a2b_hex(h))

