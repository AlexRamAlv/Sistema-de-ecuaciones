def muestra_ecuaciones(a, b, c):
  
  print(25 *'=')
  a = a 
  b = b  
  c = c
  if b < 0:
    text = 'Esta es tu ecuación: => {}x {}y = {}'
  else:
    text = 'Esta es tu ecuación: => {}x +{}y = {}'
  print(text.format(a, b, c))
  print(25 * '='+'\n')

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
        print(f' El valor de la variable x es {x}\n Y el valor de y es {y}') 

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
