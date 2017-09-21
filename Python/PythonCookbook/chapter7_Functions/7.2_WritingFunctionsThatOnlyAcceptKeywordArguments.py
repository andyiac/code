def recv(maxsize, *, block):
    'Receives a message'
    pass


# recv(1024, True)
recv(1024, block=True)


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

