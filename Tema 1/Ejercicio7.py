#Parte 1
a = [1, 2, 3]
b = a

b.append(4)

print(a) #a = [1,2,3,4] ya que b es otra forma de llamar a lo que apunta a
print(b) #b sera lo mismo que a, ya que apuntan a lo mismo

#Parte 2

a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a) #a = [1,2,3] 
print(b) #b = [1,2,3,4] ya que al haber hecho b = a.copy(), se crea un objeto nuevo que cnotiene una copia superficial del contenido de a

#Parte 3

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)

#Ambos tendran lo mismo, ya que aunque a y b son objetos distintos, comparten las mismas listas ya que b no es mas que una copia superficial de a. La lista principal de ambas es distintas pero las listas que estan dentro de la lista principal son las mismas y por tanto ambos seran [[1,2,99], [3,4]]

#Parte 4
import copy

a = [[1, 2], [3, 4]]

# Crea aquí una copia profunda llamada b
b = copy.deepcopy(a)

b[0].append(99)

print(a)
print(b)

#Parte 5

a = [1, 2, 3]

b = a
c = a.copy()

print("a == b?", a == b) #True ya que ambos apuntan a la misma lista
print("a is b?", a is b) #True por lo mismo de antes
print("a == c?", a == c) #True ya que aunque son objetos distintos por haber hecho un copy(), el contenido es el mismo
print("a is c?", a is c) #False, ya que como c es una copia de a, aunque tienen el mismo contenido ambos apuntan a listas distintas