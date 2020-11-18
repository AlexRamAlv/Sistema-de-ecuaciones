import matplotlib.pyplot as plt

def muestra_ecuaciones(a, b, c):
  
  print(45 *'=')
  a = a 
  b = b  
  c = c
  if b < 0:
    text = 'Esta es tu ecuación: => {}x {}y = {}'
  else:
    text = 'Esta es tu ecuación: => {}x +{}y = {}'
  print(text.format(a, b, c))
  print(45 * '='+'\n')

def metodo_reduccion(a, b, c, a1, b1, c1):

  if b < 0 and b1 > 0:

    a1_reducion = abs(b) * a1
    c1_reduccion = abs(b) * c1
    a_reducion = b1 * a
    c_reduccion = b1 * c


    a_dif = a_reducion + a1_reducion
    c_dif = c_reduccion + c1_reduccion
    
    x = c_dif / a_dif

    y = (c - (a * x))/ b

    print('Elegiste resolver el sistema por reduccion \n \nPaso 1: \n')
    print(f'({b1}) * {a}x + ({b1}) * {b}y = ({b1}) * {c}')
    print(f'({abs(b)}) * {a1}x + ({abs(b)}) * {b1}y = ({abs(b)}) * {c1}')
    print(45 *'-','\n v \npaso 2: \n \nSumar o restar los términos: \n')
    print(f'{a_reducion}x {b1*b}y = {c_reduccion}')
    print(f'{a1_reducion}x + {abs(b)*b1}y = {c1_reduccion}')
    print(45 *'-','\n v \npaso 3: \n \nse despeja a x de la ecuación a continuación: \n')
    print(f'{a_dif}x + 0y = {c_dif}\n')
    print(f'despeje de x = {c_dif}/{a_dif}, entonces x = {x}\n')
    print(45*'-')
    print(f'valor de x en ecuación 1: {a}*{x} + {b}y = {c}\n')
    print(f'valor de y = {c} - ({a}*({x})/{b}) \n')
    print(45*'*')
    print(f' --El valor de la variable x es {x}\n \n --Y el valor de y es {y}') 
    print(45*'*')

  elif b > 0 and b1 < 0:
    a1_reducion = b * a1
    c1_reduccion = b * c1
    a_reducion = abs(b1) * a
    c_reduccion = abs(b1) * c

    a_dif = a_reducion + a1_reducion
    c_dif = c_reduccion + c1_reduccion
    x = c_dif / a_dif
    y = (c - (a * x))/ b
    print(f' El valor de la variable x es {x}\n Y el valor de y es {y}') 

  else:
    b *= -1
    a1_reducion = b * a1
    c1_reduccion = b * c1
    a_reducion = b1 * a
    c_reduccion = b1 * c

    a_dif = a_reducion + a1_reducion
    c_dif = c_reduccion + c1_reduccion
    x = c_dif / a_dif
    y = (c - (a * x))/ (b * -1)
    print(f' El valor de la variable x es {x}\n Y el valor de y es {y}') 

def metodo_igualacion():
    pass

def metodo_sustitucion():
    pass

def metodo_grafico(a, b, c, a1, b1, c1):
  x = -10
  valores_x = []
  valores_y0 = []
  valores_y1 = []

  while x <= 20:
    y0 = (c + (-1)*a*x) / b
    y1 = (c1 + (-1)*a1*x) / b1

    valores_x.append(x)
    valores_y0.append(y0)
    valores_y1.append(y1)
    x += 1
              
  plt.plot(valores_x, valores_y0, label='Ecuacion I')
  plt.plot(valores_x, valores_y1, label='Ecuacion II')
  plt.legend()
  plt.grid()
  plt.show()