from Clases import persona

def obtenernombre (self):
        return f'Mi nombre es: {self.nombre} {self.apellido}'

p=persona("Manuel","Morillo")
print(p.obtenernombre())

