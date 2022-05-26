from IFacturaBuilder import IFacturaBuilder
from Factura import Factura

class FacturaComercial(IFacturaBuilder):

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
    
    def numeroTelefonico(self, numero) -> None:
        self._factura.add(numero)

    def personaContacto(self, pContacto) -> None:
       self._factura.add(pContacto)
    
    def nombreComercial(self, nombre) -> None:
        pass
    
    def numeroComprobante(self, numero) -> None:
        pass
    
    def domicilioComercial(self, domicilio) -> None:
        self._factura.add(domicilio)

    def nombreEmisor(self, nombre) -> None:
        self._factura.add(nombre)

    def rfcEmisor(self, rfc) -> None:
        pass

    def nombreReceptor(self, nombre) -> None:
        pass

    def rfcReceptor(self, rfc) -> None:
        pass
    
    def folioFiscalDigital(self, folioFiscalDigital) -> None:
        pass

    def fechaEmisor(self, fecha) -> None:
        pass
    
    def lugarEmisor(self, lugar) -> None:
        pass
    
    def horaEmisor(self, hora) -> None:
        pass

    def tipoCfdi(self, tipoCfdi) -> None:
        pass

