#__str__ sirve para sobrecargar el print de cara al usuario
#__repr__ sobrecarga el print para fines de depuracion
#__len__ sobrecarga la funcion len para el objeto
#__add__ sobrecarga el operador +
class Vector:
    
    def __init__(self, x=None, y=None): #Se que no hace falta, pero me apetecia añadir alguna metodo de control
        
        self.x = x
        self.y = y

    def __add__(self, otro_vector) -> "Vector":

        nuevoX = self.x + otro_vector.x
        nuevoY = self.y + otro_vector.y

        return Vector(nuevoX, nuevoY)

    def __repr__(self):

        return f"Vector({self.x}, {self.y})"

    def __str__(self):

        return f"Valor del valor x = {self.x} \nValor de y = {self.y}"

    def __len__(self):
        if self.x is None and self.y is None:
            return 0
        elif self.x is None or self.y is None:
            return 1
        else:
            return 2



vector1 = Vector(3, 2)
vector2 = Vector(2, 3)

vector3 = vector1 + vector2
print(vector3)
print(repr(vector3))

vector4 = Vector(3)

print(vector3)
print(len(vector3))
print(len(vector4))