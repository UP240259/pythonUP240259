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
