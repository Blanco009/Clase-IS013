print("Imprime las tablas de multiplicar del 1 al n.")
n = int(input("Digite un número: "))


for tabla in range(1,n+1,1):
    print("***********************************")
    print("TABLA DEL ", tabla,"\n")
    numero = 0
    while (numero<=10):
        resultado=tabla*numero
        print(tabla, " * ",numero, " = ", resultado)
        numero += 1
print("\n")
print("Gracias, fin del programa.")
