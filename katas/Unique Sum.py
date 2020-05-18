from functools import reduce

def unique_sum(lst):
    #filtered = [lst[i] for i in range(len(lst)) if lst[i] not in lst[i+1:]]
    return reduce(lambda c, e: c + e, set(lst), 0) if set(lst) else None

print(unique_sum([1,2,3,1,2,3]))

# return reduce(lambda c, l: c + 1 if l in 'aeiou' else c, inputStr, 0)