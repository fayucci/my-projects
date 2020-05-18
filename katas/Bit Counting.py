import math

def countBits(n):
    return sum([n >> k & 1  for k in range(math.ceil(math.log2(n+1)))])
    return sum(map(int , bin(n)[2:]), 0)

assert countBits(0) == 0, 'cero es cero'

assert countBits(0b001) == 1, 'uno es uno'

assert countBits(0b0101000101011) == 6, 'uno es uno'

assert countBits(0b1101) == 3, 'uno es uno'

assert countBits(0b0101) == 2, 'uno es uno'

