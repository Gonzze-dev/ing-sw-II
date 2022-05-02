from IFacturaBuilder import IFacturaBuilder
from Factura import Factura

class FacturaElectronica(IFacturaBuilder):
    
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
        pass
    
    def numeroTelefonico(self, numero) -> None:
        pass

    def personaContacto(self, pContacto) -> None:
        pass

    def nombreComercial(self, nombre) -> None:
        pass
    
    def numeroComprobante(self, numero) -> None:
        pass
    
    def domicilioComercial(self, domicilio) -> None:
        pass

    def nombreEmisor(self, nombre) -> None:
        self._factura.add(nombre)

    def rfcEmisor(self, rfc) -> None:
        self._factura.add(rfc)

    def nombreReceptor(self, nombre) -> None:
        self._factura.add(nombre)

    def rfcReceptor(self, rfc) -> None:
        self._factura.add(rfc)

    def folioFiscalDigital(self, folioFiscalDigital) -> None:
        self._factura.add(folioFiscalDigital)

    def fechaEmisor(self, fecha) -> None:
        self._factura.add(fecha)
    
    def lugarEmisor(self, lugar) -> None:
        self._factura.add(lugar)
    
    def horaEmisor(self, hora) -> None:
        self._factura.add(hora)

    def tipoCfdi(self, tipoCfdi) -> None:
        self._factura.add(tipoCfdi)