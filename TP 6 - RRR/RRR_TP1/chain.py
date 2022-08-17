from abc import ABC, abstractmethod
from datetime import datetime
from SingletonGetJson import SingletonGetJson
from historial import Historial


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    s = SingletonGetJson()
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class Token1Handler(AbstractHandler):
    saldo = 1000
    
    def handle(self, request):
        if (request["tk"] == self.s.getToken("token1")
            and request["monto"] <= self.saldo):

            self.saldo -= request["monto"]
            return {"nroPedido": request["nroPedido"],
                    "fecha": datetime.today().strftime('%Y-%m-%d'),
                    "cuenta": "cuenta1",
                    "monto": request["monto"]}
        else:
            return super().handle(request)

class Token2Handler(AbstractHandler):
    saldo = 2000
    
    def handle(self, request):
        if (request["tk"] == self.s.getToken("token2")
            and request["monto"] <= self.saldo):

            self.saldo -= request["monto"]
            return {"nroPedido": request["nroPedido"],
                    "fecha": datetime.today().strftime('%Y-%m-%d'),
                    "cuenta": "cuenta2",
                    "monto": request["monto"]}
        else:
            return super().handle(request)




def client_code(handler, requests):
    historial = Historial()
    for request in requests:
        result = handler.handle(request)
        if result is not None:
            historial.add(result)
        else:
            print("Error al realizar la transaccion")

    historial.mostrarHistorial(historial.__iter__())


if __name__ == "__main__":
    # monkey = MonkeyHandler()
    # squirrel = SquirrelHandler()
    # dog = DogHandler()

    tk1 = Token1Handler()
    tk2 = Token2Handler()

    tk1.set_next(tk2)
    requests = [{"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A1", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B1", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A2", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B2", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B3", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A3", "monto": 500}]
                
    client_code(tk1, requests)
