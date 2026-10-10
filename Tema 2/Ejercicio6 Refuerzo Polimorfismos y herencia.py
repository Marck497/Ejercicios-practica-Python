class Tarea:

    def __init__(self, titulo, prioridad=3):
        
        self.titulo = titulo
        self.prioridad = prioridad


    def resumen(self):
        return f"({self.prioridad}) {self.titulo}"


class TareaPersonal(Tarea):
    
    def resumen(self):
        return f"[PERSONAL] {super().resumen()}"

class TareaTrabajo(Tarea):
    
    def resumen(self):
        return f"[TRABAJO] {super().resumen()}"



class TareaRecurrente(Tarea):

    def __init__(self, titulo, dias, prioridad=3):
        super().__init__(titulo, prioridad)
        self.dias = dias

    def resumen(self):
        return f"{super().resumen()} [CADA {self.dias} DIAS]"


def mostrar_resumen(tareas: list) -> None:

    for tarea in tareas:
        print(tarea.resumen())


tareas = [
    TareaPersonal("Ir al médico", 2),
    TareaTrabajo("Preparar informe", 1),
    TareaRecurrente("Backup", 7, 4),
    Tarea("Comprar leche", 3)
]

mostrar_resumen(tareas)