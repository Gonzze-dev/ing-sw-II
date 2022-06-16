from random import shuffle
from Carta import Carta
from Crupier import Crupier
from Mazo import Mazo
from Integrante import Integrante
from Jugador import Jugador

def testJugador():
    c1 = Carta(11, 'A')
    c2 = Carta(10, 'J')
    c3 = Carta(2, '2')

    jugador = Integrante('Gonzalo', 'Croupier')
    jugador.addCarta(c1)
    jugador.addCarta(c2)
    jugador.addCarta(c3)

    jugador.__sumarPuntos__()

    print(jugador)

def testJugador2():
    mazo = Mazo()
    crupier = Crupier('Mauro')
    j1 = Jugador('Gonzalo')

    j1.templateAlgoritmo("1", crupier, mazo)
    print(j1.getCartas())

def testIterator():
    mazo =  Mazo()
    mazo.mezclar()
    cMazo = mazo.__iter__()
    print("len mazo: ", cMazo.len(), "\n")

    while(cMazo.len() >= 0):
        print(cMazo.__next__())

    print("len mazo: ", cMazo.len(), "\n")


print("test 1")
testJugador()

print("\ntest 2")
testJugador2()

print("\ntest 3")
testIterator()

