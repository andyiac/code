def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print("-----------")


def countdown(n):
    print('String to count down from ', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(100)

print(c)

next(c)
