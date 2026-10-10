Tarea = {
    "Nombre": "Estudiar Python",
    "Descripcion": "Repasar funciones",
    "Nivel de prioridad": 2
}

def calcular_prioridad(tarea) -> str:
    coso = tarea["Nivel de prioridad"]
    match coso:
        case 1:
            return "Muy alta"
        case 2:
            return "Alta"
        case 3:
            return "Media"
        case 4:
            return "Baja"
        case 5:
            return "Muy baja"
        case _:
            raise ValueError("Error, valor no soportado")

def mostrar_tarea(tarea) -> None:
    print(f"Nombre Tarea = {tarea['Nombre']}")
    print(f"Descripcion = {tarea['Descripcion']}")
    print(f"Nivel de prioridad = {calcular_prioridad(tarea)}")

mostrar_tarea(Tarea)

def crear_tarea() -> dict:
    nombre_tarea = input("Introduzca nombre de la tarea... ")
    descripcion_tarea = input("Introduzca descripcion breve de la tarea... ")
    prioridad_tarea = int(input("Nivel de prioridad de tarea?... "))

    nueva_tarea = {

        "Nombre" : nombre_tarea,
        "Descripcion" : descripcion_tarea,
        "Nivel de prioridad" : prioridad_tarea

    }

    return nueva_tarea

mi_tarea = crear_tarea()
mostrar_tarea(mi_tarea)