def count_sheep(n):
    list_count = [str(sheep)+" sheep..." for sheep in range(1, n+1)]
    return ''.join(list_count)
    
count_sheep(5)  