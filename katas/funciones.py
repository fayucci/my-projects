def saludo(nombre, apellido, genero):
    nombre_completo = ' ' + nombre + ' ' + apellido
    if genero == 'mujer':
        return 'hola sra ' + nombre_completo
    elif genero == 'hombre':
        return 'hola sr ' + nombre_completo
    else:
         return 'hola ' + nombre_completo 
         
print(saludo('fatima', 'yucci','mujer'))
     
print(saludo('gabriel', 'urbina', 'hombre'))
        
print(saludo('gabriel', 'urbina', 'perro'))

def merge(*dicts):
    grande = {}
    for pequeño in dicts:
        for key in pequeño.keys():
            if key in grande:
                raise Exception('There has been an error in the system')
            else:
                grande[key] =  pequeño[key]
    return grande

#print(merge({'a':1, 'b':0}, {'e':7, 'b':8}))


def merge_list(*diccionarios):
    biblioteca = {}
    for diccionario in diccionarios:
        for palabra in diccionario.keys():
            if palabra in biblioteca:
                biblioteca[palabra].append(diccionario[palabra])

            else:
                biblioteca[palabra] =  [diccionario[palabra]]
    return biblioteca

print(merge_list({'a':1, 'b':0}, {'e':7, 'b':8}))


def nb_year(p0, percent, aug, p):
    # your code
    pn = p0 
    years = 0
    while pn < p:
        pn = pn + (pn * (percent/100)) + aug
        years = years + 1
    return years


    def nb_year(pn, percent, aug, target, n=0):
    if pn >= target: return n
    else:return nb_year(pn + (pn * (percent/100)) + aug, percent, aug, target, n+1)