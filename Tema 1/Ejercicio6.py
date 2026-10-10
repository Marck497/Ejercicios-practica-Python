#Parte 1
lista_a = [1, 2, 3]
lista_b = lista_a

lista_b.append(4)

print(lista_a) #Va a sacar 1,2,3 y 4, ya que lista_b no es mas que otra forma de llamar a lista_a
print(lista_b) #Lo mismo que lista_a por lo que he explicado antes

#Parte 2

print(lista_a == lista_b) #Va a sacar True, ya que el contenido de ambos es el mismo
print(lista_a is lista_b) #Va a sacar True, por lo que he explicado antes, al ser ambos el mismo nombre para lo mismo, ambos apuntan a la misma lista

#Parte 3

def modificar(lista) -> None:
    # Haz que la lista tenga también el número 4
    lista.append(4)

numeros = [1, 2, 3]

modificar(numeros)

print(numeros)

#Parte 4

def modificar(numero) -> int:
    # Incrementa numero en 1
    numero = numero + 1 #No va a modificar al parametro de entrada, simplemente va a crear otro numero y no va a salir a no ser que le de un return a la funcion
    return numero #Se que no es necesario para el ejercicio pero me daba toc que no sirviera para nada la funcion

valor = 10

modificar(valor)

print(valor)