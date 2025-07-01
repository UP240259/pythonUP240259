#Ejercicios nivel 1.
tupla = tuple()
hermanos = ("Kenai","Angel","David","Alejandro","Alan", "Junior")
hermanas =("Noemi","Amilenix","Yamileth","Kimora","Ruth","Herlinda")
siblings = hermanas + hermanos
print(siblings)
print("i have ", len(siblings), "siblings.")
family_mambers = hermanas + hermanos
print(family_mambers)



#Ejercicios nivel 2
fruits = ("apple","orange","pear","grape","Mango")
vegetables = ("Cucumber","Potato","Carrot","Cabage","Tomato")
animals = ("Milk","Eggs","Honey","Butter","steak")
food_stuff_tp = fruits + vegetables + animals
food_stuff_tp_lst = list(food_stuff_tp)
print(food_stuff_tp_lst[5:10])
print(food_stuff_tp_lst[:3])
print(food_stuff_tp_lst[-3:])
print("primeros tres y ultimos tres itemsde la lista: ",food_stuff_tp_lst[:3]+food_stuff_tp_lst[-3:])
del food_stuff_tp
#print(food_stuff_tp) #no existe porque se acaba de eliminar la tupla del codigo

nordic_countries = ("Denmark","Finland","Iceland","Norway","Sweden",)
print("Estonia" in nordic_countries) #Devuelve false.
print("Iceland" in nordic_countries) #Devuelve true.

