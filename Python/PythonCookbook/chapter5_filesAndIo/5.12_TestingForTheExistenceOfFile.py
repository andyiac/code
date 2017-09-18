import os

import time

print(os.path.exists('/etc/passwd'))

print(os.path.exists('/tmp/spam'))

print(os.path.isfile('/etc/passwd'))

print(os.path.isdir('/etc/passwd'))

print(os.path.islink('/usr/local/bin/python3'))

print(os.path.getsize('/etc/passwd'))

print(time.ctime(os.path.getmtime('/etc/passwd')))

print(time.ctime(os.path.getatime('/etc/passwd')))
print(time.ctime(os.path.getctime('/etc/passwd')))
