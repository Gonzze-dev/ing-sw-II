from SetUpBlanco import ConcreteFactorySetUpBlanco
from SetUpNegro import ConcreteFactorySetUpNegro 
from client_code import client_code

print("Client: Testeando client code con el primer tipo de factory:")
client_code(ConcreteFactorySetUpBlanco())

print("\n")

print("Client: Testeando client code con el segundo tipo de factory:")
client_code(ConcreteFactorySetUpNegro())