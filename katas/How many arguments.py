def args_count(*args, **kargs):
    return len(args) + len(kargs)

assert args_count() == 0, 'si no le pasas ningun argumento debe ser cero'

assert args_count(1) == 1

assert args_count(1, 2) == 2

assert args_count(32, a1=12) == 2, 'si paso un argumento de orden y otro de nombre debe ser 2'
assert args_count(None) == 1, 'te comiste un mambo'