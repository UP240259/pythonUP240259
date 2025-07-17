#Ejercicio nivel 2.
my_age = int(input("Ingresa tu edad: "))

your_age = int(input("Ingresa tu edad: "))

if my_age > your_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print("Soy un año mayor que tu.")
    else: 
        print(f"soy {diferencia} años mayor que tu.")
elif your_age > my_age:
    difference = your_age - my_age
    if difference ==1:
        print("Eres un año mayor que yo.")
    else:
        print(f"Eres {difference} años mayor que yo.")
else:
    print("Tenemos la misma edad.")
