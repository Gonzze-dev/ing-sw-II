from abc import ABC
from Carta import Carta

#template
class Integrante(ABC):

    def __init__(self, nombre, rol) -> None:
        self._nombre = nombre
        self._rol = rol
        self._puntaje = 0
        self.cartas = []
    
    def templateAlgoritmo(self, opcion, crupier, mazo):
        if opcion == "1":
            carta = self.sacarCarta(mazo, crupier)
            self.addCarta(carta)
        elif opcion == "2":
            self.__sumarPuntos__()

    def getNombre(self):
        return self._nombre
    
    def getRol(self):
        return self._rol
    
    def getPuntaje(self):
        return self._puntaje
    
    def getCartas(self):
        return self.cartas
    
    def addCarta(self, carta):
        if carta is not None:
            self.cartas.append(carta)
            pass

    def __addPuntaje__(self, puntaje):
        self._puntaje += puntaje

    def __sumarPuntos__(self):
        contPuntos = 0
        cartaAs = None

        for carta in self.cartas:
            if (carta.getPinta()[0] != 'A'):
                contPuntos += carta.getValor()
            else:
                cartaAs = carta

        if cartaAs is not None:
            if (contPuntos > 10):

                contPuntos += 1
                self.__addPuntaje__(contPuntos)
            else:

                contPuntos += cartaAs.getValor()
                self.__addPuntaje__(contPuntos)
        else:
            self.__addPuntaje__(contPuntos)
    
    def sacarCarta(self, mazo, crupier = None):
        pass

    def __str__(self) -> str:
        strIntegrante = ("Nombre: " + self._nombre + "\n" +
                         "Rol: " + self._rol + "\n" +
                         "Puntaje: " + str(self._puntaje))

        return strIntegrante