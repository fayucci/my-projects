def normalize(x):
    return 0 if x <= 0 else x if x < 255 else 255
def to_hex(n):
    return hex(normalize(n))[2:].zfill(2).upper()

def rgb(r, g, b):
    return to_hex(r) + to_hex(g) + to_hex(b) 


assert rgb(0,0,0) == '000000', 'si son ceros debe ser cero'

assert rgb(1,0,0) == '010000', 'deberia retornar eso'

assert rgb(1, 1, 0) == '010100'

assert rgb(1, 1, 1) == '010101'

assert rgb(-1, 1, 1) == '000101', rgb(-1,1,1)

assert rgb(-1, -1, -1) == '000000'

assert rgb(256, 1, 1) == 'FF0101', rgb(256, 1, 1)

assert rgb(256, 256, 256) == 'FFFFFF'