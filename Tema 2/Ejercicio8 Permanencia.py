import json
from pathlib import Path

class Tarea:
    
    def __init__(self, titulo: str, prioridad: int = 3):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def a_dict(self) -> dict:

        tareaDict = {

            "titulo" : self.titulo,
            "prioridad" : self.prioridad,
            "completada" : self.completada

        }

        return tareaDict

    @classmethod
    def from_dict(cls, diccionario:dict) -> "Tarea":

        nuevaTarea = cls(diccionario["titulo"], diccionario["prioridad"])
        nuevaTarea.completada = diccionario.get("completada", False)
        return nuevaTarea


def guardar_tareas(tareas:list[Tarea], ruta:Path) -> None:

    datos = []

    for tarea in tareas:

        datos.append(tarea.a_dict())

    texto_json = json.dumps(datos, ensure_ascii=False, indent=2)
    ruta.write_text(texto_json, encoding="utf-8")

def cargar_tareas(ruta:Path) -> list[Tarea]:

    if not ruta.exists():
        return []

    datos = json.loads(ruta.read_text(encoding="utf-8")) #Lista de diccionarios
    
    listaTarea = []
    
    for dato in datos:
        listaTarea.append(Tarea.from_dict(dato))

    return listaTarea
    

def main():
    # El JSON estará junto a este archivo Python
    ruta = Path(__file__).resolve().parent / "tareas.json"

    # Recuperamos las tareas guardadas anteriormente
    tareas = cargar_tareas(ruta)

    print(f"Se han cargado {len(tareas)} tareas.")

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Añadir tarea")
        print("2. Mostrar tareas")
        print("3. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")

            try:
                prioridad = int(input("Prioridad (1-5): "))
            except ValueError:
                print("La prioridad debe ser un número entero.")
                continue

            if not 1 <= prioridad <= 5:
                print("La prioridad debe estar entre 1 y 5.")
                continue

            nueva_tarea = Tarea(titulo, prioridad)
            tareas.append(nueva_tarea)

            guardar_tareas(tareas, ruta)
            print("Tarea añadida y guardada.")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas guardadas.")
            else:
                for numero, tarea in enumerate(tareas, start=1):
                    estado = "Completada" if tarea.completada else "Pendiente"
                    print(
                        f"{numero}. {tarea.titulo} "
                        f"(Prioridad: {tarea.prioridad}) - {estado}"
                    )

        elif opcion == "3":
            guardar_tareas(tareas, ruta)
            print("Datos guardados. Cerrando el programa.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
