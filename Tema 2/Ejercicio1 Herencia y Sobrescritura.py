class Tarea:

    def __init__(self, titulo, prioridad=3):
        self.titulo = titulo
        self.prioridad = prioridad

    def resumen(self):
        return f"[{self.prioridad}] {self.titulo}"

class TareaRecurrente(Tarea):
   
    def __init__(self, titulo, dias, prioridad=3):
        super().__init__(titulo, prioridad)
        self.dias = dias

    def resumen(self):
        return super().resumen() + f", Dias que se repite = {self.dias}"

t1 = Tarea("Estudiar Python", 3)
t2 = TareaRecurrente("Copia de seguridad", 7, 5)
t3 = TareaRecurrente("Revisar apuntes", 2)

print(t1.resumen())
print(t2.resumen())
print(t3.resumen())