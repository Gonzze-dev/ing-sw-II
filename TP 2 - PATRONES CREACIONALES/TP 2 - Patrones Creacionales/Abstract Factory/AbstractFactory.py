from __future__ import annotations
from abc import ABC, abstractmethod
from AbstractProductMonitor import AbstractProductMonitor
from AbstractProductMouse import AbstractProductMouse
from AbstractProductTeclado import AbstractProductTeclado

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductMonitor:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductMouse:
        pass

    @abstractmethod
    def create_product_c(self) -> AbstractProductTeclado:
        pass