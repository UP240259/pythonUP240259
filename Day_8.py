empty_dict = {}

#Example.
person = {
    "Nombre:" : "José de Jesús",
    "Apellidos" : "Hernández Gutiérrez",
    "Edad" : 20,
    "País" : "México",
    "is_married" : False,
    "Skills" :["Java","python","MongoDB","Node"],
    "address" : {
        "street" : "Bismuto",
        "Codigo_postal" : "99960"
}
}


#Ejercicios: Día 8.

#1
dog = {} #como no tiene ningun elemento dentro, no mostrara nada.

#2
dog["Nombre"] = "Chiquilina" #Agrega elemento a un diccionario.
dog["Color"] = "Café"
dog["Cama"] = "Blanca"
dog["Piernas"] = "chiquitas"
dog["Edad"] = 7
print(dog)

#3
estudiante = {
    "Nombre" : "José de Jesús",
    "Apellidos" : "Hernández Gutiérrez",
    "Edad" : 20,
    "Casado" : False,
    "Skills" : ['JavaScript', 'React', 'Node',
'MongoDB', 'Python'],
    "Dirección" : {
        "País" : "México",
        "Ciudad" : "Aguacalientes",
        "Colonia" : "San Gerardo"
    }
}
print(estudiante)

#4
print(len(estudiante)) #Muestra cuantos items hay en el diccionario.

#5
student = list(estudiante["Skills"]) #Esto solo convierte la llave y los items en una lista.
print(type(student))

#6
estudiante["Skills"] = "C++" #Agrega un item en la llave que te gustaría agregarla.
print(estudiante)

#7
llaves = estudiante.keys() #Solo convierte las llaves del diccionario en lista.
print(llaves)

#8
values = estudiante.values() #Convierte los valores del diccionario en una lista.
print(values)

#9
print(estudiante.items()) #Esto cambia el diccionario a una lista de tuplas.

#10
del estudiante["Edad"] #Elimina uno de los items que estan dentro del diccionario.
print(estudiante)

#11
print(dog) #no va a mostrar nada en pantalla porque acaba de ser eliminado.
del dog


