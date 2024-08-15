Vuelo = {
    'Aerolinea' : 'Avianca' ,
    'Vuelo' : 'AV3102' ,
    'Origen' : 'CTG' ,
    'Destino' : 'MDE' ,
    'Tipo_maleta' :  ['Cabina' , 'Mano' , 'Bodega']
    
}

print("Datos del Vuelo")
for key, value in Vuelo.items():
    print(f"{key} : {value}")
    
print("\nDatos de la maleta")
for Maleta in Vuelo["Tipo_maleta"]:
    print(Maleta)
