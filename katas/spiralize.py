
def print_matrix(matrix):
    for row in matrix: print(' '.join(str(e) for e in row))

class list2d(list):
	def __getitem__(self, accessor):
		if isinstance(accessor, tuple): 
			[i, j] = accessor
			if i < 0 or j < 0: return
			try: return self[i][j]
			except IndexError: return
		else: return super().__getitem__(accessor)

	def __setitem__(self, accessor, value):
		if isinstance(accessor, tuple): 
			[i, j] = accessor
			if i < 0 or j < 0: return
			try: self[i][j] = value
			except IndexError: return
		else: return super().__setitem__(accessor, value)

def spiralize(size):
    spiral = list2d([[1 for j in range(size)] for i in range(size)])
    i = 1
    j = -1

    while True:
        if spiral[i, j+1] == 0: break
        if spiral[i, j+2] != 1: break
        while spiral[i, j+2] == 1: 
            spiral[i,j+1] = 0
            j = j + 1

        if spiral[i+1, j] == 0: break
        if spiral[i+2, j] != 1: break
        while spiral[i+2, j] == 1: 
            spiral[i+1,j] = 0
            i = i + 1

        if spiral[i, j-1] == 0: break
        if spiral[i, j-2] != 1: break
        while spiral[i, j-2] == 1: 
            spiral[i,j-1] = 0
            j = j - 1

        if spiral[i-1, j] == 0: break
        if spiral[i-2, j] != 1: break
        while spiral[i-2, j] == 1: 
            spiral[i-1,j] = 0
            i = i - 1
    return spiral


print_matrix(spiralize(8))