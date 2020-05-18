def square_sum(numbers):
    return sum(map(lambda num: num**2, numbers))


assert square_sum([0, 0, 0]) == 0, square_sum([0, 0, 0])

assert square_sum([1, 0, 0]) == 1, 'uno es uno'

assert square_sum([1, 2, 2]) == 9, 'uno es uno'