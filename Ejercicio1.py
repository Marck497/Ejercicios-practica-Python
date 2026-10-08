nombre_tarea = input("Intoduzca nombre de Tarea: ")
descripcion_tarea = input("Dame una descripcion breve de dicha tarea: ")
nivel_prioridad = int(input("Indique el nivel de prioridad de dicha tarea"))
tipo_prioridad = "Si estas viendo esto es que algo ha salido mal"

while(nivel_prioridad < int(1)) or (nivel_prioridad > int(5)):
    nivel_prioridad = int(input("ERROR, Valor no soportado, vuelva a itentarlo"))

if(nivel_prioridad == int(1)):
    tipo_prioridad = "Muy Alta"
elif(nivel_prioridad == int(2)):
    tipo_prioridad = "Alta"
elif(nivel_prioridad == int(3)):
    tipo_prioridad = "Media"
elif(nivel_prioridad == int(4)):
    tipo_prioridad = "Baja"
elif(nivel_prioridad == int(5)):
    tipo_prioridad = "Muy Baja"

nuevaTarea = {

    "Nombre" : nombre_tarea,
    "Descripcion" : descripcion_tarea,
    "Nivel de prioridad" : nivel_prioridad

}

print(f"Nombre Tarea =  {nuevaTarea['Nombre']}")
print(f"Descripcion = {nuevaTarea['Descripcion']}")
print(f"Nivel de prioridad = {tipo_prioridad}")
