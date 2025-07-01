#Ejercicios nivel 1.
#1
it_companies = {"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
companies = len(it_companies)
print(companies)

#2
it_companies.add("Twitter")
print(it_companies) #Agrega un item al set.

#3
it_companies.update(["Sephora","Nike","KFC"])
print(it_companies) #muestra mas compañias.

#4
it_companies.remove("Twitter") #Remueve un item.
print(it_companies)

#5
it_companies.pop() #Descarta un item random
print(it_companies)


#Ejercicios nivel 2.
A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}

#1
union = A.union(B)
print(union)

#2
Intersection = A.intersection(B) #Escoje los items que esten en ambas variables.
print(Intersection)

#3
subject1 = B.issubset(A)
print(subject1)

subject2 = A.issubset(B)
print(subject2)

#4
disjoint1 = B.isdisjoint(A)
print(disjoint1)

disjoint2 = A.isdisjoint(B)
print(disjoint2)

#5
A_with_B = A.union(B)
print(A_with_B) #Une A con B.

B_with_A = B.union(A)
print(B_with_A) #Une B con A.

#6
symetric1 =B.symmetric_difference(A)
print(symetric1)

symetric2 = A.symmetric_difference(B)
print(symetric2)

#7
del A #Eliminara A

del B #Eliminara B


#Ejercicios nivel 3.

#1
age = [22,19,24,25,26,24,25,24]
print(len(age)) #Es mas grande la lista porque tiene datos duplicados.

sete = set(age)
print(len(sete)) #Es mas pequeña proque quita los datos duplicados.

#2
#El estring es un tipo de dato que solo es texto, mientras que las listas se pueden modificar
#Tambien se pueden tener datos duplicados, mientras que en las tuplas no pueden ser modificadas.
#El conjunto no puede tener datos duplicados ni se puede modificar.

#3
frase = "I am a teacher and I love to inspire and teach people."
word = frase.split()
palbras_unicas = set(word)
print("palbras unicas: ", palbras_unicas)
print("Número de palbras unicas: ", len(palbras_unicas))






