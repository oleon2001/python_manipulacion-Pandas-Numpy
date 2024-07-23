import random

def generador_contraseña():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    contraseña = ""
    for i in range(8): 
        contraseña += random.choice(caracteres)
    return contraseña
print(generador_contraseña())



pronombre = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {'yo': 'o', 'tu': 'as', 'el': 'a', 'nosotros': 'amos', 'vosotros': u'áis', 'ellos': 'an'}

palabra = input(u'Verbo regular 1ra. conjugación: ')
for i in pronombre:
    print (i, palabra[0:len(palabra)-2] + terminaciones[i])