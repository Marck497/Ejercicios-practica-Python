def repartir_cerezas(num_cerezas, num_personas):

    try:
      
        resultado = num_cerezas/num_personas

    except ZeroDivisionError:

        print("ERROR, no se puede dividir por cero")

    else:

        print(f"Cada persona recibe {resultado} cerezas")

    finally:

        print("Fin del reparto")


repartir_cerezas(12, 3)
repartir_cerezas(12, 0)

class PrioridadInvalida(Exception):
    pass

def validar_prioridad(prioridad):

    if not(1 <= prioridad <= 5):
        raise PrioridadInvalida("La prioridad debe estar entre 1 y 5")

    return prioridad


try:
    print(validar_prioridad(3))
except PrioridadInvalida as e:
    print(f"Error: {e}")

try:
    print(validar_prioridad(8))
except PrioridadInvalida as e:
    print(f"Error: {e}")