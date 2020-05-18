def triangle(row):
    if len(row) <= 1: return row
    next_row = [
        i if i == j else (set('RGB') - set((i,j))).pop()
        for (i,j) in zip(row, row[1:])
    ] 

    print(''.join(next_row))
    return triangle(''.join(next_row))


triangle('RRGBRGBB')

#print(set('RGB').difference(set('RG')).pop())