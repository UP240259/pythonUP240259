#Día 9: Condicionales (if, else, elsif).

#Ejercicio nivel 1.
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres lo suficiente grande para manejar.")
else:
    print("No eres lo suficiente grande para manejar.")

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


# Ejercicio nivel 3.
personas = {
    "Nombre": "José de Jesús",
    "Apellido": "Hernández Gutiérrez",
    "Edad": 20,
    "País": "México",
    "Casado": False,
    "Skills": ["Python", "Java", "React", "Node", "MongoDB"],
    "Dirección": {
        "Calle": "Mulberry street",
        "CP": "99960"
    }
}

# 1. Mostrar la habilidad del medio
if "Skills" in personas:
    skills = personas["Skills"]
    medio = len(skills) // 2
    print("Middle skill:", skills[medio])

# 2. Verificar si tiene Python
if "Skills" in personas:
    tiene_python = "Python" in personas["Skills"]
    print("Tiene la habilidad con Python:", tiene_python)

# 3. Detectar tipo de desarrollador
if "Skills" in personas:
    skills_set = set(personas["Skills"])
    if set(["JavaScript", "React"]).issubset(skills_set):
        print("He is a front end developer")
    elif set(["Node", "Python", "MongoDB"]).issubset(skills_set):
        print("He is a backend developer")
    elif set(["React", "Node", "MongoDB"]).issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. Verificar si está casado y vive en México
if personas.get("Casado") and personas.get("País") == "México":
    nombre = personas["Nombre"]
    pais = personas["País"]
    print(f"{nombre} is married and lives in {pais}.")