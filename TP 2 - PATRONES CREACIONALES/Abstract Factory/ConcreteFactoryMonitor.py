from AbstractFactory import AbstractFactory
from AbstractProductMonitor import AbstractProductMonitor
from MonitorBlanco import MonitorBlanco
from MonitorNegro import MonitorNegro

class ConcreteFactoryMonitor(AbstractFactory):
    def crear_producto_a(self) -> AbstractProductMonitor:
        return MonitorBlanco()
    
    def crear_producto_b(self) -> AbstractProductMonitor:
        return MonitorNegro()