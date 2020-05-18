from collections import Counter
print(Counter('fatimita'))

def duplicate_count(text):
    return len([letter for letter in set(text.lower()) if text.lower().count(letter) > 1])

assert duplicate_count('') == 0, 'esta vacio'

assert duplicate_count('a') == 0, 'no se repite nada'

assert duplicate_count('aa') == 1, 'se repite1'

assert duplicate_count('aabb') == 2, 'se repiten 2'

assert duplicate_count('aa1123ghj') == 2, 'se repiten 2'