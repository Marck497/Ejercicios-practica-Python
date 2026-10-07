#Parte 1:
punto = (("x", 10), ("y", 20))

for valor in punto:
    print(f"{valor[0]} = {valor[1]}")

#Parte 2 sin set
Cosas = ["Python", "Programacion", "Python", "VHDL", "Programacion"]
Cosas.append("Universidad")

for cosa in Cosas:
    print(cosa)

numDeVeces = int(0)

for cosa in Cosas:
    if(cosa == "Python"):
        numDeVeces = numDeVeces + 1

print(f"La palabra Python se encuentra {numDeVeces} veces")

numDeVeces = int(0)

for cosa in Cosas:
    if(cosa == "Java"):
        numDeVeces = numDeVeces + 1

print(f"La palabra Java se encuentra {numDeVeces} veces")

#Parte 2 convirtiendo la lista Cosas a set

setCosas = set(Cosas)
palabraBuscada = "Python"

if palabraBuscada in setCosas:
    
    print(f"{palabraBuscada} se encuentra en Cosas")

else:

    print(f"{palabraBuscada} no se encuentra en Cosas")

palabraBuscada = "Java"

if palabraBuscada in setCosas:
    
    print(f"{palabraBuscada} se encuentra en Cosas")

else:

    print(f"{palabraBuscada} no se encuentra en Cosas")

#Parte 3
numeros = [5,2,8,2,5,9]

for numero in numeros:
    print(numero)

numeros.append(10)

print(f"Actualmente en la lista hay {len(numeros)} elementos. El primer elemento de la lista es: {numeros[0]} y el ultimo es {numeros[-1]}")