from functools import reduce

def getCount(inputStr):
    return reduce(lambda c, l: c + 1 if l in 'aeiou' else c, inputStr, 0)

print(getCount('cfghj'))
