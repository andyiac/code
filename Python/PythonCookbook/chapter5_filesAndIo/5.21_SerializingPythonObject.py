import pickle
import urllib.request

# u = {'andyiac':"zhang", 'test': 'asdfasd'}
#
# f = open('somefile', 'wb')
# pickle.dump(u, f)

restore = open('somefile','rb')
data = pickle.load(restore)
print(data)
