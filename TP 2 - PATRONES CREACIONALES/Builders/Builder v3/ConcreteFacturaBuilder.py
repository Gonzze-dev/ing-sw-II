from IFacturaBuilder import IFacturaBuilder
from Factura import Factura

class ConcreteFacturaBuilder(IFacturaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._factura = Factura()

    @property
    def factura(self) -> Factura:
        factura = self._factura
        self.reset()
        return factura
    
    def dirCorreoElectronico(self, dirCorreo) -> None:
        self._factura.add(dirCorreo)
        return self

    def numeroTelefonico(self, numero) -> None:
        self._factura.add(numero)
        return self

    def personaContacto(self, pContacto) -> None:
        self._factura.add(pContacto)
        return self

    def nombreComercial(self, nombre) -> None:
        self._factura.add(nombre)
        return self

    def numeroComprobante(self, numero) -> None:
        self._factura.add(numero)
        return self
    
    def domicilioComercial(self, domicilio) -> None:
        self._factura.add(domicilio)
        return self

    def nombreEmisor(self, nombre) -> None:
        self._factura.add(nombre)
        return self

    def rfcEmisor(self, rfc) -> None:
        self._factura.add(rfc)
        return self

    def nombreReceptor(self, nombre) -> None:
        self._factura.add(nombre)
        return self

    def rfcReceptor(self, rfc) -> None:
        self._factura.add(rfc)
        return self

    def folioFiscalDigital(self, folioFiscalDigital) -> None:
        self._factura.add(folioFiscalDigital)
        return self

    def fechaEmisor(self, fecha) -> None:
        self._factura.add(fecha)
        return self

    def lugarEmisor(self, lugar) -> None:
        self._factura.add(lugar)
        return self

    def horaEmisor(self, hora) -> None:
        self._factura.add(hora)
        return self

    def tipoCfdi(self, tipoCfdi) -> None:
        self._factura.add(tipoCfdi)
        return self
        
