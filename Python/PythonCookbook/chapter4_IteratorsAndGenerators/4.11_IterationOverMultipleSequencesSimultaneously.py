xpts = [1, 5, 4, 2, 10]
ypts = [101, 78, 37, ]

print('--------len 1----', len(xpts))
print('---------len 2-----', len(ypts))

for x, y in zip(xpts, ypts):
    print(x, y)

from itertools import zip_longest

for x, y in zip_longest(xpts, ypts):
    print(x, y)
