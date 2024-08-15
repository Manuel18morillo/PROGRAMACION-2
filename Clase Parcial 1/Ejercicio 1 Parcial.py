class animales:
    def __init__(self,nombre,numeropatas,fechavacuna,propietario):
        self.nombre = nombre
        self.numeropatas = numeropatas
        self.fechavacuna  = fechavacuna
        self.propietario = propietario
             
    def obtenernombre(self):
        print("su nombre es: ",self.nombre)
        
    def obtenerpatas(self):
        print("su numero de patas es:",self.numeropatas)
        
    def Obtener_vacuna(self):
        print("Su vacuna es: ",self.fechavacuna)
        
    def obtenerPropietario(self):
        print("su propietario es : ", self.propietario)
        
x = animales ("Luna" , 4 , "12/08/23" , "Manuel")
x.obtenernombre()
x.obtenerpatas()
x.Obtener_vacuna()
x.obtenerPropietario()