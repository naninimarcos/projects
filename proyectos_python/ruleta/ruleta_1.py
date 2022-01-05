# sin minimo de tiradas
""" 
----------- INFORMACION --------------------------
Aplicacion que recrea una ruleta y grafica sus resultados, 
la intencion de esta es ser una base para proyectos de prediccion no lineales en un futuro
"""

import matplotlib.pyplot as plt
import random

"------ importaciones de modulos --------------"
"------ variables a utilizar --------------"
lista = []
i = 0
i1 = 0
i0 = 0
a = 0
i1 = 0
z = 0
#########################################################################################################################
"------ las 4 listas, 2 son dinamicas y 2 estaticas --------------"
ss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sb = list(range(37))
sxb = ['cero', 'par', 'diferencia', 'impar']
sx = [0, 0, 0, 0]
#########################################################################################################################
"------ definiciones --------------"


def tirada():
    a = random.randint(0, 36)
    lista.append(a)
    ss[a] = int(ss[a]) + 1
    if a == 0:
        sx[0] = int(sx[0]) + 1
    elif a % 2 == 0:
        sx[1] = int(sx[1]) + 1
    else:
        sx[3] = int(sx[3]) + 1
    return


"------ funciones 1 --------------"
c = int(input("cantidad de vueltas a hacer: "))
while i1 != c:
    b = 0
    i = 0
    i0 = 0
    b = int(input("cantidad de tiradas a hacer: "))
    z = z + b
    i1 = i1 + 1

    if b == 0:
        i1 = c

    else:
        while i != b:
            tirada()
            i = i + 1
        ####################################
"""
------ funciones 2 --------------
terminado el desarrollo de funciones1 es que trabajamos ahora el graficar los datos"""

sx[2] = sx[1] - sx[3]
"------ q total de veces que salio cada datos --------------"
plt.bar(sb, ss, color="blue", linewidth=10, label="linea")
plt.legend()
plt.show()

while i0 != 37:
    print("la cantida de veces que salio el numero {}, fueron {} veces ".format(
        sb[i0], ss[i0]))
    i0 = i0 + 1

print(sb)
print(ss)
"------ q total de veces que salio par o impar --------------"
plt.bar(sxb, sx, color="red", linewidth=4, label="s")
plt.legend()
plt.show()
print(sxb)
print(sx)
print(z)
xxx = [i / int(z) for i in ss]
print(xxx)
print(sum(xxx))
"------ probabilidad por frecuencia __ x1/qtotal  --------------"
plt.bar(sb, xxx, color="blue", linewidth=10, label="linea")
plt.legend()
plt.show()
##############################################
