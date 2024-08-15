class lote:
    def __init__(self, largo, ancho, constructora):
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora
        
    def calcular_Area(self):
        print(self.largo * self.ancho)     

class casa(lote):
    def __init__(self, largo, ancho, propietario ,constructora  ,telefono):
        super().__init__(largo, ancho, constructora)
        self.propietario = propietario
        self.telefono = telefono
    
        
    def printpropietario(self):
        print(self.propietario)
        
    def printtelefono(self):
        print(self.telefono)
        
    def printconstructora(self):
        print(self.constructora)
    
x = casa(14, 50, "Manuel Morillo ", "NameIndefined" , "3009813543")  
x.calcular_Area()
x.printpropietario()
x.printconstructora()
x.printtelefono() 

