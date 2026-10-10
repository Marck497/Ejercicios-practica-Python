from abc import ABC, abstractmethod

# Completa aquí Notificador

class Notificador(ABC):

    @abstractmethod
    def enviar(self, mensaje:str) -> str:
        ...

# Completa aquí NotificadorEmail

class NotificadorEmail(Notificador):

    def enviar(self, mensaje):
        return (f"Email enviado: {mensaje}")

notificador = NotificadorEmail()
print(notificador.enviar("La tarea ha terminado"))

class NotificadorSMS:
    
    def enviar(self, mensaje:str) -> str:
        return f"SMS enviado: {mensaje}"

def avisar(notificadores:list, mensaje: str) -> None:

    for cosa in notificadores:
        print(cosa.enviar(mensaje))


notificadores = [
    NotificadorEmail(),
    NotificadorSMS()
]

avisar(notificadores, "La tarea ha terminado")