def filter_list(l):
    return list(filter(lambda x: type(x)!= str, l))

print(filter_list([1,2,'a','b']))