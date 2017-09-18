import os

names = os.listdir('/')
print(names)

# get all regular files
names = [name for name in os.listdir('/')
         if os.path.isfile(os.path.join('/', name))]
print(names)

# Get all dirs

dirnames = [name for name in os.listdir('/')
            if os.path.isdir(os.path.join('/', name))]
print(dirnames)

import glob

pyfiles = glob.glob('*.py')
print(pyfiles)

from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('.')
           if fnmatch(name, '*.py')]
print(pyfiles)


