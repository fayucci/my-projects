def buffer(itr, size):
    cache = []
    for value in itr:
        cache.append(value)
        if len(cache) == size:
            yield cache
            cache = []
    if len(cache):
        yield cache

assert str(list(buffer([0, 1, 2, 3],2))) == str([[0, 1], [2,3]]), list(buffer([0, 1, 2, 3],2))

assert str(list(buffer([0, 1, 2, 3],1))) == str([[0], [1], [2], [3]]), list(buffer([0, 1, 2, 3],1))

assert str(list(buffer([0, 1, 2, 3, 4],2))) == str([[0, 1], [2,3], [4]]), list(buffer([0, 1, 2, 3, 4],2))
