###indices!
##
##Materiales=["Libros:","Cuadernos:","Lapiceros:","Cartuchera:"]
##Precios=[0]*4 # que hay una lista con cuatro espacios, pero vacios,
###Precios=[0,0,0,0]
##
##
##print("Digite los valores a asignar para los siguientes items: ")
##for posicion in range(0,4):
##    
##    for valor in range (0,4):
##        if posicion == valor:
##            Precios[posicion]=int(input(Materiales[valor]))
##            print("\n",Materiales, Precios, posicion, valor,"\n")
##
##

Articulos = ["Impresora", "Monitor", "Teclado"]
Precios = []*3


print("Digite los valores a asignar para los siguientes items: ")

for objeto in range(0,3):
    for valor in range(0,3):
        if objeto == valor:
            Precios[objeto] = int(input(Articulos[valor]))
            print("\n",Articulos, Precios, objeto, valor,"\n")


