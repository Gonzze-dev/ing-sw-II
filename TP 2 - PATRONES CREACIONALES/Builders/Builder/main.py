from Director import Director
from FacturaComercial import FacturaComercial
from IFacturaBuilder import IFacturaBuilder
from FacturaElectronica import FacturaElectronica

director = Director()
facturaElectronicaBuilder = FacturaElectronica()
facturaComercialBuilder = FacturaComercial()

director.builder = facturaElectronicaBuilder

print("Factura electronica ")

director.buildFacturaElectronica('Gonzalo', '123', 'Emi', '1245', '17/03/05',
'25 de mayo 168', '17:30', 'A')

facturaElectronicaBuilder.factura.listar_partes()

print()
print('Factura Comercial')
director.builder = facturaComercialBuilder
director.buildFacturaComercial('Gonzalo', '25 de mayo 123', 'Clara', '3446507537', 'errandoneagonzalo18@gmail.com')
facturaComercialBuilder.factura.listar_partes()