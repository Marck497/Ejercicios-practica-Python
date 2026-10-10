class Tarea:
    def __init__(self, titulo, prioridad=3):
        self.titulo = titulo
        self.prioridad = prioridad

    @property
    def titulo(self):
        return self._titulo

    @property
    def prioridad(self):
        return self._prioridad

    @titulo.setter #Soy consciente de que no es necesario todo esto de los setter en este atributo pero queria practicarlo para asentar
    def titulo(self, nombre) -> None:
        
        if (1 <= len(nombre) <= 20):
            self._titulo = nombre
        else:
            raise ValueError("ERROR demasiados caracteres para un titulo")

    @prioridad.setter
    def prioridad(self, valor):

        if (1 <= valor <= 5):
            self._prioridad = valor
        else:
            raise ValueError("ERROR valor no soportado")

    @staticmethod #Basicamente es para crear una funcion que este relacionada con la clase pero en este caso no hace falta instanciar un nuevo objeto de dicha clase para usarla, se usa desde fuera como si fuera una funcion gobal pero comprar cosas de la funcion donde se creo
    def prioridad_valida(valor):
        if (1 <= valor <= 5):
            return True
        else:
            return False

    @classmethod #Para crear constructores alternativos, basicamente estas sobrecargando la funcion para inicializarla con otro tipos de datos. cls significa un objeto de esta clase
    def desde_dict(cls, datos) -> "Tarea":
        
        return cls(datos["titulo"],datos["prioridad"])

print(Tarea.prioridad_valida(3))
print(Tarea.prioridad_valida(10))

datos = {
    "titulo": "Estudiar Python",
    "prioridad": 5
}

tarea = Tarea.desde_dict(datos)

print(tarea.titulo)
print(tarea.prioridad)
