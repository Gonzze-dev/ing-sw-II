from abc import ABC, abstractmethod

from SingletonGetJson import SingletonGetJson


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
        if request["tk"] == self.s.getToken("token1"):
            return ("entro")
        else:
            return super().handle(request)




def client_code(handler):

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print("\nClient: Who wants a " + food + "?")
        result = handler.handle(food)
        if result:
            print(result)
        else:
            print(food + " was left untouched.")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog\n")
    client_code(monkey)
    print("\n")

    # print("Subchain: Squirrel > Dog\n")
    # client_code(squirrel)
    # print("\n")
