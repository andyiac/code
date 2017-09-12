# 手动消耗掉迭代器

# with open('/etc/passwd') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line)
#     except StopIteration:
#         pass

with open('/etc/passwd') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line)
