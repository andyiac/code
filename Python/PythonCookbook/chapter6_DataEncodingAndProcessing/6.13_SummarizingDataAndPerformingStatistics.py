import os

import pandas

file_path = os.path.expanduser('~/Downloads/rats.csv')
print(file_path)
rats = pandas.read_csv(file_path, skip_footer=1)
print(rats)

