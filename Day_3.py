Edad= 19
altura= 1.78
numero_complejo= 3 + 4j

# Ejercicio 1
base= int(input("Ingresa la base del triángulo: "))
altura= int(input("ingresa la altura del triángulo: "))
area= (base*altura/2)
print("el aréa del triángulo es: ", area)

# Ejercicio 2
print("Ingresa los valores de los lados del triángulo")
a= int(input("lado a: "))
b= int(input("lado b:"))
c= int(input("lado c: "))
perimetro= a+b+c
print("El perimetro del triángulo es: ", perimetro)

print("Ingresa el valor del ancho del rectángulo")
ancho= float(input("ancho: "))
print("Ingresa el valor del largo del rectángulo")
largo= float(input("Largo: "))
area_rectangulo= ancho*largo
perimetro_rectangulo= (2*ancho)+(2*largo)
print("El área del rectángulo es: ", area_rectangulo)
print("El perímetro del rectángulo es: ", perimetro_rectangulo)

# Ejercicio 3
print("Ingresa el valor del radio del círculo")
radio= int(input("Radio: "))
Area_circulo= 3.1416*radio**2
print("El ára del circulo es: ", Area_circulo)

# Ejercicio 4
print("Ingresa el valor del radio del circulo: ")
radio= int(input("Radio: "))
Circunferencia= (2*3.1416)*radio
print("la circunferencia del circulo es: ", Circunferencia)

# Ejercicio 5
x1,y1 = 0, -2
x2,y2 = 1, 0

pendiente= (y2-y1)/(x2-x1)
print("La pendiente de la recta es: ", pendiente)

# Ejercicio 6
x1, y1= 2, 2
x2, y2= 6, 10
pendiente= (y2-y1)/(x2-x1)
print("La pendiente de la recta es: ", pendiente)

# Ejercicio 7
print("Comparación de resultados")
if pendiente == pendiente:
    print("Los resultados son iguales")
else:
    print("Los resultados son diferentes")








# ejercicio 8
print("Encuentre el valor de y")
for x in range(-1, 3):
    y= x**2 + 6*x + 9
    print("El valor de y es: ", y)
    if y== 0:
        print("El valor de y es cero cuano x vale: ", x)

# Ejercicio 9

palabra_1 = "python"
palabra_2 = "dragon"
longitud_1 = len(palabra_1)
longitus_2 = len(palabra_2)
if longitud_1 > longitus_2:
    print("La palabra python es más larga que dragon")
else:
    print("La palabra dragon es más larga que python")

# Ejercicio 10
sentence= "i hope this course is not full of jargon"
if "jargon" in sentence:
    print("La palabra 'jargon' está en la oración.")
else:
    print("La palabra 'jargon' no está en la oración.")
print("jargon" in sentence)

# Ejercicio 11
on= ("on" in palabra_1) and ("on" in palabra_2)
print("¿Ambas palabras contienen la palabra 'on'? ", on)

# Ejercicio 12
longitud_1_float = float(longitud_1)
longitud_1_str = str(longitud_1_float)
print("Tipo de longitud_1_float:", type(longitud_1_float))
print("Tipo de longitud_1_str:", type(longitud_1_str))

# Ejercicio 13
n= int(input("Ingresa un número entero:"))
if n % 2==0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 14
r= (7//3) == int(2.7)
print("El resultado de la comparación es:", r)

# Ejercicio 15
print(type("10") == type(10))

# Ejercicio 16
print("Es 9.8 igual a 10?")
num= int(float("9.8"))
print(num==10)
print("Es falso, porque 9.8 no es igual a 10")

# Ejercicio 17
worked_hours = int(input("Ingrese las horas trabajadas: "))
hourly_rate = float(input("Ingrese la paga por hora: "))
pago_semanal = worked_hours * hourly_rate
print("El pago semanal es: ", pago_semanal)

# Ejercicio 18
def años_a_segundos(años):
    segundos_por_año = 365 * 24 * 60 * 60
    return años * segundos_por_año

años_usuario = int(input("Ingresa el número de años que quieres calcular: "))

vida_maxima = 100

segundos_vida = años_a_segundos(vida_maxima)

print(f"Una persona que vive {vida_maxima} años vive aproximadamente {segundos_vida} segundos.")

segundos_usuario = años_a_segundos(años_usuario)
print(f"En {años_usuario} años hay aproximadamente {segundos_usuario} segundos.")

# Ejercicio 19
print("N  1  N  N^2  N^3")
for n1 in range(1, 6):
    print(f"{n}  1  {n}  {n**2}  {n**3}")










