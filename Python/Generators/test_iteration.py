class countdown(object):
    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r


for x in countdown(10):
    print(x)
