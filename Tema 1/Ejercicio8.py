#Parte 1
def añadir_tarea(tareas=[]):
    tareas.append("Nueva tarea")
    return tareas

print(añadir_tarea())
print(añadir_tarea())
print(añadir_tarea())

#Parte 2
def añadir_tareas(tareas=None) -> list:
    if tareas is None:
        tareas = []

    tareas.append("Nueva tarea")
    return tareas

print(añadir_tareas())
print(añadir_tareas())
print(añadir_tareas())

#Parser sintactico PDL 2