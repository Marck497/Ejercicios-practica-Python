class Tarea:
    def __init__(self, titulo, descripcion, prioridad=3):
        
        self._titulo = titulo
        self._descripcion = descripcion
        self.prioridad = prioridad
        self._completada = False

    @property #Es la forma de engoblar tanto el setter como el getter. Cada uno se llama dependiendo de como se use. OJO hay que definirle a python que es el setter con el @atributo.setter
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        if not(1 <= valor <=5):
            raise ValueError("Error, valor no contemplado")

        self._prioridad = valor

tarea = Tarea("Estudiar Python", "Repasar propiedades", 3)

print(tarea.prioridad)

tarea.prioridad = 5
print(tarea.prioridad)

#tarea.prioridad = 10 los comentarios los he puesto despues de comprobarlo por consola para que no lance un error
#print(tarea.prioridad)

#self._prioridad = valor, lo que estas haciendo es modificar DIRECTAMENTE el atributo que esta guardado con el nombre _prioridad sin pasar por el setter
#al usar self.prioridad = valor, lo que hace python es buscar y llamar al setter para modificar el atributo