class factura:
    def __init__(self,id,vendedor,fechacompra):
        self.id=id
        self.vendedor=vendedor
        self.fechacompra=fechacompra   
    
    def ob_vendedor(self):
        print("El vendedor es: ",self.vendedor)
        
    def ob_fechacompra(self):
        print("La fecha de compra es:",self.fechacompra)
        
        
class detallefactura(factura):
    def __init__(self,id,vendedor,fechacompra,producto,cantidad,precio):
        super().__init__(id,vendedor,fechacompra)
        self.producto=producto
        self.precio=precio
        self.cantidad=cantidad
        
        
    def ObtenerDatosCompras(self):
        print("El id es: " , self.id,"\nel producto es un: " , self.producto)
        
    def Calculartotal1(self):
        self.total = self.cantidad*self.precio
        print("El total es: ",self.total)
        
x=detallefactura(23423, "manuel","21/34/342" , "carros corporation" , 120000000 ,4) 
x.ob_vendedor()
x.ob_fechacompra()  
x.ObtenerDatosCompras()
x.Calculartotal1()   

