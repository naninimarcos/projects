# precisa interasiones hasta completar los 37 espacios
""" 
----------- INFORMACION --------------------------
Aplicacion que recrea una ruleta y grafica sus resultados, 
la intencion de esta es ser una base para proyectos de prediccion no lineales en un futuro
"""
""" 
----------- cambios--------------------------
es igual que el primer codigo solo que se trabajo con numpy y se busca simplificar el codigo,
precisa que salgan todos los numeros de caso contrario los graficos no se realizan. por eso puede tener problemas en tiradas pequeñas 
"""

import matplotlib.pyplot as plt
import numpy as np
import random
lista = []
i = 0
i1 = 0
i0 = 0
a = 0
#########################################################################################################################
sb = list(range(37))
sxb = ['cero', 'par', 'diferencia', 'impar']
sx = [0, 0, 0, 0]
#########################################################################################################################


def tirada():
    a = random.randint(0, 36)
    lista.append(a)
    if a == 0:
        sx[0] = int(sx[0]) + 1
    elif a % 2 == 0:
        sx[1] = int(sx[1]) + 1
    else:
        sx[2] = int(sx[3]) + 1
    return


c = int(input("cantidad de vueltas a hacer: "))
while i1 != c:
    b = 0
    i = 0
    i0 = 0
    b = int(input("cantidad de tiradas a hacer: "))
    i1 = i1 + 1
    if b == 0:
        i1 = c
    else:
        while i != b:
            tirada()
            i = i + 1
        ####################################
sx[2] = sx[1] - sx[3]
aa = list(np.bincount(lista))
plt.bar(sb, aa, color="blue", linewidth=3, label="q")
plt.legend()
plt.show()
while i0 != 37:
    print("la cantida de veces que salio el numero {}, fueron {} veces ".format(
        sb[i0], aa[i0]))
    i0 = i0 + 1

print(aa)
print(sb)
plt.bar(sxb, sx, color="red", linewidth=4, label="s")
plt.legend()
plt.show()
print(sxb)
print(sx)
##############################################
