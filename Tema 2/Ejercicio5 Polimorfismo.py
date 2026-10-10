class Tarea:
    
    def __init__(self, titulo:str):
        self.titulo = titulo

    def resumen(self):
        return self.titulo


class TareaPersonal(Tarea):

    def __init__(self, titulo):
        super().__init__(titulo)

    def resumen(self):
        return (f"[PERSONAL] {super().resumen()}")


class TareaTrabajo(Tarea):
    
    def __init__(self, titulo):
        super().__init__(titulo)

    def resumen(self):
        return f"[TRABAJO] {super().resumen()}"

listaTareas = [

TareaPersonal("Ir al médico"),
TareaTrabajo("Preparar informe"),
Tarea("Comprar leche")

]

for tarea in listaTareas:
    print(tarea.resumen())