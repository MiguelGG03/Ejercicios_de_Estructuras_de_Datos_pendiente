class Producto:

    def __init__(self,naturaleza):
        self.naturaleza=naturaleza








def main():
    producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
    precio_neto = FactoryFactura.crear(producto).facturar() 
    print(precio_neto) 
    # 105.5 
    
    producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
    precio_neto = FactoryFactura.crear(producto).facturar() 
    print(precio_neto) 
    # 120 

if __name__=='__main__':
    main()