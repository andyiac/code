import os

path = '/Users/andyiac/Data/data.csv'

# get the last component of the path
base_name = os.path.basename(path)
print('- base name ---->', base_name)


join_path = os.path.join('temp', 'data', os.path.basename(path))
print("join path --->", join_path)


path2 = '~/Data/data.csv'
expanduser_path = os.path.expanduser(path)
print("--expanduser ---->", expanduser_path)

split_path = os.path.splitext(path2)
print(split_path)

