class Tarea:
    def __init__(self, titulo, descripcion, prioridad=3):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__completada = False

    def completar(self) -> None:
        self.__completada = True

    def mostrar(self) -> None:
        print(f"Titulo: {self.__titulo}")
        print(f"Descripcion: {self.__descripcion}")
        print(f"Prioridad: {self.__prioridad}")
        print(f"Completada: {self.__completada}")

tarea_python = Tarea("Estudiar Python", "Pues eso xd, estudiar python no se bro", 5)
tarea_ejercicio = Tarea("Hacer ejercicio", "5 flexiones, 4 sentidallas y 2 abdominales")

tarea_python.mostrar()
tarea_ejercicio.mostrar()

tarea_python.completar()
tarea_python.mostrar()
