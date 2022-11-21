
#Maneras de romper un ciclo


##numero = float(input("Ingrese un número. y digite 0 para terminar: "))
##
##while (numero !=0):
##    numero = float(input("ingresa un número. 0 para  terminar: "))
##print("Fin del programa")


while (True):
    numero = float(input("Ingresar numero, si quiere terminar dijite cero: "))

    if (numero == 0):
        break

print("Fin programa")
