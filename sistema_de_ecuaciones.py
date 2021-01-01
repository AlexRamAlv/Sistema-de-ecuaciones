import metodos as mtd
import time

""" 
    Estas lines de código calcula sistemas de ecuaciones lineales con dos incógnitas
    Solo se debe ingresar los coeficientes de cada ecuacion según se solicite
    Las ecuaciones tienen la forma: ax + by = c
    
"""

#ecuación no 1
print('\n Digita los coeficientes\n')
a = float(input('Coeficeinte de X1: '))
b = float(input('Coeficeinte de Y1: '))
c = float(input('Término independiente de la ecuacion 1: '))

mtd.muestra_ecuaciones(a, b, c)

#ecuación no 2
a1 = float(input('Coeficeinte de X2: '))
b1 = float(input('Coeficeinte de Y2: '))
c1 = float(input('Término independiente de la ecuacion 2: '))

#método que muestra las ecuaciones

mtd.muestra_ecuaciones(a1, b1, c1)

#método de reducción
tiempo_inicial = time.time()
mtd.metodo_reduccion(a, b, c, a1, b1, c1)
tiempo_final = time.time()
print(f'\n--el tiempo de resolver el sistema de ecuaciones fue de {tiempo_final - tiempo_inicial}--')

#método gráfico
# tiempo_inicial = time.time()
mtd.metodo_grafico(a, b, c, a1, b1, c1)
# tiempo_final = time.time()
# print(f'el tiempo que duraste con el gráfico abierto fue de {tiempo_final - tiempo_inicial}')



