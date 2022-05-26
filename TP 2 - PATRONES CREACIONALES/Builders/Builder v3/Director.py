from IFacturaBuilder import IFacturaBuilder

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> IFacturaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IFacturaBuilder) -> None:
        self._builder = builder

    def buildFacturaElectronica(self, nombreEmisor, rfcEmisor, nombreReceptor,
    rfcReceptor, fechaEmisor, lugarEmisor, horaEmisor, tipoCfdi) -> None:
    
        self.builder.nombreEmisor(nombreEmisor).rfcEmisor(rfcEmisor).nombreReceptor(nombreReceptor).rfcReceptor(rfcReceptor).fechaEmisor(fechaEmisor).lugarEmisor(lugarEmisor).horaEmisor(horaEmisor).tipoCfdi(tipoCfdi)
    
    def buildFacturaComercial(self, nombreEmisor, domicilioComercial, personaContacto, 
    numeroTelefono, dirCorreo) -> None:

        self.builder.nombreEmisor(nombreEmisor).domicilioComercial(domicilioComercial).personaContacto(personaContacto).numeroTelefonico(numeroTelefono).dirCorreoElectronico(dirCorreo)

