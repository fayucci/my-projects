def flatten_and_sort(array):
    return sorted([item for sublist in array for item in sublist])

print(flatten_and_sort( [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))