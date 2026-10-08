tareas = ["Estudiar Python", "Hacer ejercicio", "Comprar comida", "Repasar VHDL"]

for i, tarea in enumerate(tareas):
    print(f"{i + 1}. {tarea}")

condicion_nuevaTarea = (input("Desea sumar una nueva tarea? si -> Si; cualquier otra cosa -> No").lower())

while condicion_nuevaTarea == "si":

    nuevaTarea = input("Introduzca nueva tarea: ")
    tareas.append(nuevaTarea)
    condicion_nuevaTarea = (input("Desea sumar una nueva tarea? si -> Si; cualquier otra cosa -> No").lower())

print("Total de tareas: ")
for i, tarea in enumerate(tareas):
    print(f"{i + 1}. {tarea}")

