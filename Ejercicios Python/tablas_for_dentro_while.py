print("Imprime las tablas de multiplicar del 1 al n.")
n = int(input("Digite un número: "))

tabla = 1

while (tabla <= n):
    print("\nTABLA DEL ", tabla, "\n")
    for numero in range(0,11,1):   
        resultado=tabla*numero
        print(tabla, " * ",numero, " = ", resultado)
        numero += 1
    tabla += 1

        
print("\n")
print("Gracias, fin del programa.")
