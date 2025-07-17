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
word = frase.split() #El .split() sirve para separar el string en partes más pequeñas.
palbras_unicas = set(word) #Aquí ponemos el set() para convertir las palabras en conjunto.
print("palbras unicas: ", palbras_unicas)
print("Número de palbras unicas: ", len(palbras_unicas)) #Ponemos len() para contar cuantas palabras unicas tiene el conjunto.