#Parte 1
def crear_tarea(titulo, prioridad=3, urgente=False) -> dict:
    mi_tarea = {

        "titulo" : titulo,
        "prioridad" : prioridad,
        "urgente" : urgente

    }

    return mi_tarea

miTarea1 = crear_tarea("Estudiar Python")
miTarea2 = crear_tarea("Estudiar Python", 5)
miTarea3 = crear_tarea("Estudiar Python", urgente=True)

print(miTarea1)
print(miTarea2)
print(miTarea3)

#Parte 2
miTarea4 = crear_tarea(prioridad=5, urgente=True, titulo="Comprar patatas")
print(miTarea4)

#Parte 3
mensaje = "Global"

def probar():
    mensaje = "Local"
    print(mensaje)

probar() #Sacara por pantalla Local ya que primero busca la variable local
print(mensaje) #Sacara por pantalla Global ya que local no se encuentra en su scope

def probar():
    global mensaje
    mensaje = "modificacion de global"
    print(mensaje)

probar()
print(mensaje)