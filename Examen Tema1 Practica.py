# Parte C. Implementaciones cortas — 2 puntos
# 4 ejercicios · 0,5 puntos cada uno

# C1. Función de clasificación
# Implementa:
# def calcular_prioridad(nivel: int) -> str:
# Debe devolver:
# Nivel	Resultado
# 1 o 2	"Baja"
# 3	"Media"
# 4 o 5	"Alta"
# Para cualquier valor fuera del intervalo de 1 a 5, debe lanzar ValueError.

def calcular_prioridad(nivel: int) -> str:
    
    if nivel >= 1 or nivel <= 2:
        return "Baja"
    elif nivel == 3:
        return "Media"
    elif nivel >= 4 or nivel <= 5:
        return "Alta"
    else:
        raise ValueError("ERROR valor no contemplado")

# C2. Contar tareas completadas
# Implementa una función que reciba una lista de diccionarios con esta estructura:
# tareas = [
#     {"titulo": "Estudiar", "completada": True},
#     {"titulo": "Practicar", "completada": False},
#     {"titulo": "Repasar", "completada": True}
# ]
# La función debe devolver el número de tareas completadas.
# No debe modificar la lista original.

def num_tareas_completada(dictTareas: dict) -> int:
    
    resultado = 0
    
    for tarea in dictTareas:
        if(tarea["completada"] == True):
            resultado += 1

    return resultado


# C3. Propiedades y validación
# Implementa una clase Tarea con un atributo prioridad que:
# - tenga un valor por defecto de 3;
# - solo admita valores del 1 al 5;
# - utilice @property y @prioridad.setter;
# - lance ValueError si se intenta asignar un valor inválido.
# Explica por qué debes almacenar el valor en _prioridad dentro del setter.

class Tarea:

    def __init__(self, prioridad=3):

        self.prioridad = prioridad

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        if not(1 <= valor <= 5):
            raise ValueError("ERROR, valor no soportado")

        self._prioridad = valor

# C4. Métodos especiales
# Implementa una clase Vector con coordenadas x e y que permita:
# - sumar dos vectores mediante +;
# - mostrar una representación técnica como Vector(3, 4) mediante repr();
# - mostrar un texto descriptivo mediante print();
# - devolver 2 mediante len(vector).

class Vector:

    def __init__(self, x:int, y:int) -> None:

        self.x = x
        self.y = y

    def __add__(self, other) -> "Vector":

        return(Vector((self.x + other.x), (self.y + other.y)))

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"Vector con 2 valores:\nValor X = {self.x}\nValor Y = {self.y}"

    def __len__(self) -> int:
        return 2

# Parte D. Proyecto práctico integrador — 4 puntos
# Proyecto: Gestor de tareas personales

# Tu objetivo es desarrollar un pequeño programa de gestión de tareas desde cero. No basta con escribir fragmentos aislados: debes construir una solución coherente que combine funciones, colecciones, referencias, clases, encapsulamiento y métodos especiales.
# Especificación funcional
# El programa debe gestionar una colección de tareas. Cada tarea tendrá:
# - título;
# - descripción;
# - prioridad entre 1 y 5;
# - estado, que será pendiente o completada;
# - una colección de etiquetas sin duplicados.
# Debes implementar los siguientes requisitos.
# D1. Clase Tarea — 1 punto
# Crea la clase con:
# - un constructor que reciba título, descripción y prioridad por defecto 3;
# - título obligatorio, con entre 1 y 50 caracteres;
# - prioridad validada mediante @property y setter;
# - estado inicial pendiente;
# - un conjunto (set) para las etiquetas;
# - un método completar() que cambie el estado;
# - un método añadir_etiqueta(etiqueta) que evite duplicados.
# Los datos deben almacenarse mediante atributos de instancia. Puedes utilizar atributos con _ para el almacenamiento interno cuando sea apropiado.
# D2. Representación y métodos auxiliares — 0,75 puntos
# Añade a Tarea:
# - __str__, para mostrar la tarea de forma legible;
# - __repr__, para mostrar una representación técnica;
# - un @staticmethod llamado prioridad_valida(valor);
# - un @classmethod llamado desde_dict(cls, datos).
# El método desde_dict debe crear una tarea a partir de un diccionario. Si falta la prioridad, utilizará 3; si faltan las etiquetas, utilizará un conjunto vacío.
# D3. Funciones de gestión — 0,75 puntos
# Implementa estas funciones fuera de la clase:
# def añadir_tarea(tareas, tarea):
#     ...

# def buscar_tarea(tareas, titulo):
#     ...

# def contar_completadas(tareas):
#     ...

# def filtrar_por_prioridad(tareas, prioridad_minima):
#     ...

# Comportamiento esperado:
# - añadir_tarea incorpora una tarea a la colección.
# - buscar_tarea devuelve la tarea cuyo título coincide, o None si no existe.
# - contar_completadas devuelve el número de tareas completadas.
# - filtrar_por_prioridad devuelve una nueva lista con las tareas cuya prioridad sea igual o superior a la indicada.
# La función de filtrado no debe modificar la colección original.
# D4. Programa principal — 0,75 puntos
# Implementa un programa que:
# 1. Cree al menos tres tareas, dos de ellas a partir de diccionarios.
# 2. Añada etiquetas a varias tareas, incluyendo una etiqueta repetida.
# 3. Complete al menos una tarea.
# 4. Guarde todas las tareas en una lista.
# 5. Muestre todas las tareas.
# 6. Busque una tarea por título.
# 7. Muestre cuántas tareas están completadas.
# 8. Filtre las tareas por una prioridad mínima y muestre el resultado.
# Organiza el programa con:
# if __name__ == "__main__":    ...



# D5. Referencias, mutabilidad y calidad — 0,75 puntos
# Además del funcionamiento anterior, tu solución debe cumplir lo siguiente:
# - No debe utilizar listas o diccionarios mutables como valores por defecto.
# - La validación de prioridad debe aplicarse tanto al construir una tarea como al modificarla.
# - La búsqueda no debe devolver una copia de la tarea: debe devolver la tarea encontrada.
# - El filtrado debe devolver una lista nueva, sin alterar la original.
# - Las etiquetas repetidas no deben almacenarse más de una vez.
# - Utiliza anotaciones de tipo donde consideres apropiado y nombres descriptivos.
# Restricciones del proyecto
# - No utilices librerías externas.
# - No utilices herencia ni patrones de diseño: todavía no forman parte de este bloque.
# - No copies soluciones de Internet.
# - Puedes utilizar list, dict, set, funciones, clases, excepciones, propiedades y métodos especiales estudiados.
# - Puedes dividir el código en varias funciones y probarlo por etapas.
# Cómo entregar el examen
# Te recomiendo resolverlo en este orden:
# 1. Partes A y B: responde por escrito.
# 2. Parte C: envía el código de cada ejercicio.
# 3. Parte D: implementa el proyecto y envíame el código completo.
# Puedes entregarlo por partes; no es necesario escribir todo de una vez. Corregiré cada sección, indicaré qué está bien, qué debes modificar y qué nota obtienes.
# La nota final será sobre 10, con especial atención al proyecto integrador. Si el programa funciona pero presenta problemas conceptuales —por ejemplo, recursión accidental en un setter, copias innecesarias o un valor por defecto mutable—, también se tendrán en cuenta.
# Comienza por la Parte A, preguntas A1–A5. No te daré las soluciones antes de que las intentes.