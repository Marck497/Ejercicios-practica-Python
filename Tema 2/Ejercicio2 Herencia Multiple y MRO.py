class Tarea:
    def __init__(self, titulo:str, prioridad=3):
        self.titulo = titulo
        self.prioridad = prioridad

    def resumen(self):
        return f"[{self.prioridad}] {self.titulo}"


class Notificable:

    def notificar(self):
        print("Enviando notificacion")

class Archivable:

    def archivar(self):
        print("Archivando Tarea")

class TareaCompleta(Tarea, Notificable, Archivable):

    def __init__(self, titulo, prioridad=3):
        super().__init__(titulo, prioridad)

tarea = TareaCompleta("Repasar Tema 2", 4)

print(tarea.resumen())
tarea.notificar()
tarea.archivar() 

print(TareaCompleta.__mro__)

class NotificableID:

    def notificar(self):
        print("Enviando notificacion")

    def identificar(self):
        return "Id notificacion"

class ArchivableID:

    def archivar(self):
        print("Archivando Tarea")

    def identificar(self):
        return "Id archivar"

class TareaCompletaID(Tarea, NotificableID, ArchivableID): #Se ejecutara primero Id notificacion debido a MRO, como Notificable es la primera que se hereda, los metodos de esta tienen prioridad sobre las otras clases

    def __init__(self, titulo, prioridad=3):
        super().__init__(titulo, prioridad)

tareaID = TareaCompletaID("Repasar Tema 2", 4)

print(tareaID.identificar())

class TareaCompletaID2(Tarea, ArchivableID, NotificableID): #Se ejecutara primero Id notificacion debido a MRO, como Archivable es la primera que se hereda, los metodos de esta tienen prioridad sobre las otras clases

    def __init__(self, titulo, prioridad=3):
        super().__init__(titulo, prioridad)

tareaID2 = TareaCompletaID2("Repasar Tema 2", 4)

print(tareaID2.identificar())
