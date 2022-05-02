from AbstractFactory import AbstractFactory

def client_code(factory: AbstractFactory) -> None:
    monitor = factory.create_product_a()
    mouse = factory.create_product_b()
    teclado = factory.create_product_c()
    total = 0.00

    #Monitor
    print(monitor.getNombre())
    print(monitor.getColor())
    print(monitor.getResolucion())
    print(monitor.getCosto())
    print()
    
    #Mouse
    print(mouse.getNombre())
    print(mouse.getColor())
    print(mouse.getDPI())
    print(mouse.getCosto())
    print()
    
    #Teclado
    print(teclado.getNombre())
    print(teclado.getColor())
    print(teclado.getIdioma())
    print(teclado.getPorcentajeTeclas(), "%")
    print(teclado.getCosto())
    print()

    #total
    total = monitor.getCosto() + mouse.getCosto() + teclado.getCosto()
    print("TOTAL: ", total)