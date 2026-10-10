class Tarea:
    
    def __init__(self, titulo):
        self.titulo = titulo

class Proyecto:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaTareas = []

    def add_tarea(self, tarea:Tarea):
        self.listaTareas.append(tarea)

    def crear_tarea(self, titulo):
        nuevaTarea = Tarea(titulo)
        self.listaTareas.append(nuevaTarea)

tarea1 = Tarea("Repasar herencia")

proyecto = Proyecto("Tema 2")
proyecto.add_tarea(tarea1)
proyecto.crear_tarea("Repasar composición")

print(proyecto.nombre)
print(proyecto.listaTareas[0].titulo)
print(proyecto.listaTareas[1].titulo)

# Responde brevemente a estas dos preguntas:
# 1. ¿Por qué proyecto.anadir(tarea1) representa agregación en nuestro ejemplo?

    #Porque lo que hace es añadir una tarea ya creada a sus atributos internos     

# 2. ¿Qué diferencia hay entre esa operación y proyecto.crear_tarea("Repasar composición")?

    #Porque lo que hace es crear y añadir una nueva tarea dados unos parametros
    