print("Imprime las tablas de multiplicar del 1 al n.")
n = int(input("Digite un número: "))


#pasos para conformar el ciclo while
#variable en valor inicial
#while (condición con la variable y el valor final)
# incremente / decremente


tabla = 1
while (tabla <= n):

    print("TABLA DEL ", tabla)
    numero=0
    
    while (numero<=10):
        resultado=tabla*numero
        print(tabla," * ",numero," = ", resultado)
        numero+=1

    tabla += 1
print("Gracias")
    
