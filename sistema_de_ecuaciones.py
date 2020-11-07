import metodos as mtd

"""vamos a calcular sistemas de ecuaciones lineales con dos incógnitas'
Solo necesitas ingresar los coeficientes de cada ecuacion segun se solicite'
Las ecuaciones tienen la forma: ax + by = c"""

#ecuación no 1
print('\n Digita los coeficientes\n')
a = int(input('Coeficeinte de X1: '))
b = int(input('Coeficeinte de Y1: '))
c = int(input('Término independiente de la ecuacion 1: '))

mtd.muestra_ecuaciones(a, b, c)

#ecuación no 2
a1 = int(input('Coeficeinte de X2: '))
b1 = int(input('Coeficeinte de Y2: '))
c1 = int(input('Término independiente de la ecuacion 2: '))

mtd.muestra_ecuaciones(a1, b1, c1)

#metodo de reducción
mtd.metodo_reduccion(a, b, c, a1, b1, c1)

