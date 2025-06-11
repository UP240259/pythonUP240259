age= int(19) 
height= float(1.78)
n_complejo= complex (3 + 4j)
#area de un triángulo

base= int(input("Ingrresa la base del triangúlo: "))
altura=int(input("Ingresa la altura del triangúlo: "))
area= (base*altura/2)
print("El area del triangúlo es: ", area)

#perimetro de un triángulo

a=int(input("Introduce un valor al lado a: "))
b=int(input("Introduce un valor al lado b: "))
c=int(input("Introduce un valor al lado c: "))
perimetro= a+b+c
print("El perimetro del triánguilo es: ", perimetro)

#area y perimetro de un rectangúlo

widght=int(input("Ingresa el ancho del rectángulo: "))
length=int(input("Ingresa el largo del rectángulo: "))
area_rectangulo= widght*length
perimetro_rectangulo= 2*(widght+length)
print("El area del rectángulo es: ", area_rectangulo)
print("El perimetro del rectángulo es: ", perimetro_rectangulo)

#area y perimetro de un circulo

import math
radio=int(input("Ingresa el radio del circulo: "))
area_circulo= math.pi*(radio**2)
perimetro_circulo= 2*math.pi*radio
print("El area del circulo es: ", area_circulo)
print("El perimetro del circulo es: ", perimetro_circulo)

#pendiente de la recta y=2x-2
x1, y1 = 0, -2
x2, y2 = 1, 0
pendiente = (y2 - y1) / (x2 - x1)
print("La pendiente de la recta y=2x-2 es: ", pendiente)

#pendiente con los puntos (2,2) (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente2 = (y2 - y1) / (x2 - x1)
print("La pendiente con los puntos (2,2) (6,10) es: ", pendiente2)

# Comparación de resultados
resultado1 = 2 * 3 + 5
resultado2 = 4 + 3 * 2
print("Resultado de 2 * 3 + 5: ", resultado1)
print("Resultado de 4 + 3 * 2: ", resultado2)
print("¿Los resultados son iguales?", resultado1 == resultado2)

# Valores de x
for x in range(-5, 6):
    y = x**2 + 6*x + 9
    print(f"El valor de y para x={x} es: {y}")
    if y == 0:
        print(f"El valor de y es cero cuando x vale: {x}")

# Comparación de palabras
if palabra1 == palabra2:
    print("Las palabras son iguales.")
else:
    print("Las palabras son diferentes.")

# Comparación de palabras
if palabra1 in palabra2:
    print(f"La palabra '{palabra1}' está contenida en '{palabra2}'.")
else:
    print(f"La palabra '{palabra1}' no está contenida en '{palabra2}'.")

# Comparación de palabras
if palabra1 > palabra2:
    print(f"La palabra '{palabra1}' es mayor que '{palabra2}'.")
elif palabra1 < palabra2:
    print(f"La palabra '{palabra1}' es menor que '{palabra2}'.")

# Comparación de palabras
if palabra1.startswith('p'):
    print(f"La palabra '{palabra1}' comienza con 'p'.")
else:
    print(f"La palabra '{palabra1}' no comienza con 'p'.")
# Comparación de palabras
if palabra2.endswith('n'):
    print(f"La palabra '{palabra2}' termina con 'n'.")
else:
    print(f"La palabra '{palabra2}' no termina con 'n'.")

