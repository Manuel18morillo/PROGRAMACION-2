print ( "\nElija una opcion ")


print("\nMenu: ")
print("\n1.personas" , "\n2.vehiculos" , "\n3.universidades" , "\n4.notas" , "\n5.salir")

personas = "personas"
vehiculos = "vehiculos"
universidades="universidades"
notas="notas"
salir="salir"

x=1

while x < 5:
    
    x = int (input("Digite numero: "))
    
    if x==1:
        print("la opcion que eligiste es" , personas)
    if x == 2:
        print("La opcion que eliogiste es" , vehiculos)
    if x==3:
        print("la opcion que eligiste es" , universidades)    
    if x==4:
        print("la opcion que eligiste es" , notas)
else :
    print("Eligiste la opcion " , salir)
    