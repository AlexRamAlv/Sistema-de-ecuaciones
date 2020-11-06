def ecuaciones(a, b, c):
  print('Ecuacion #1')
  print(25 * '=')
  a = a 
  b = b  
  c = c
  text = 'Esta es tu ecuación: => {}x + {}y = {}'
  print(text.format(a, b, c))
  print(25 * '=')

"""vamos a calcular sistemas de ecuaciones lineales con dos incógnitas'
Solo necesitas ingresar los coeficientes de cada ecuacion segun se solicite'
Las ecuaciones tienen la forma: ax + by = c"""

print('Dame los coeficientes de la 1era ecuación:')
a = int(input('Coeficeinte 1: '))
b = int(input('Coeficeinte 2: '))
c = int(input('Coeficeinte 3: '))

ecuaciones(a, b, c)

print('Dame los coeficientes de la 2da ecuación:')
a1 = int(input('Coeficeinte 1: '))
b1 = int(input('Coeficeinte 2: '))
c1 = int(input('Coeficeinte 3: '))

ecuaciones(a1, b1, c1)