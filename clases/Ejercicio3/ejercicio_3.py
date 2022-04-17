from enum import Enum


class Producto:

    def __init__(self,naturaleza):
        self.naturaleza=naturaleza

    def facturar(self):
        if(isinstance(self.naturaleza,Naturaleza.ALIMENTARIA)==True):
            return 100 + (100*0.055)
        elif(isinstance(self.naturaleza,Naturaleza.SERVICIO)==True):
            return 100 + (100*0.2)


class Naturaleza(Enum):

    ALIMENTARIA=0.055
    SERVICIO=0.2


class FactoryFactura:
        
    def crear(self,producto):
         print()




class FactoryFactura: 
 
    def crear(self,naturaleza): 
        if(isinstance(self.naturaleza,Naturaleza.ALIMENTARIA)==True):
            return 100 + (100*0.055)
        elif(isinstance(self.naturaleza,Naturaleza.SERVICIO)==True):
            return 100 + (100*0.2) 
 


class Factura(FactoryFactura): 
 
    def facturar(self,naturaleza):
        if(isinstance(self.naturaleza,Naturaleza.ALIMENTARIA)==True):
            return 100 + (100*0.055)
        elif(isinstance(self.naturaleza,Naturaleza.SERVICIO)==True):
            return 100 + (100*0.2) 
 
class ModoRelease(FactoryFactura): 
 
    # Método de creación de un DiarioDeAbordo 
    # dedicado al modo Release. 
    def crear_diario(self): 
        return DiarioRelease() 
 
    def crear_representacion(self): 
        return RepresentacionRelease() 




def main():

    producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
    precio_neto = FactoryFactura.crear(producto).facturar() 
    print(Naturaleza.ALIMENTARIA)
    print(precio_neto)
    # 105.5 
    
    producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
    precio_neto = FactoryFactura.crear(producto).facturar() 
    print(precio_neto) 
    # 120 


if __name__=='__main__':
    main()