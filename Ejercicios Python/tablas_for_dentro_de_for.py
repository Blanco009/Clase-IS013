
print("Imprime las tablas de multiplicar del 1 al 3")

for tabla in range(1,4,1):
    print("***********************************")
    print("TABLA DEL ", tabla,"\n")
    
    for num in range(0,11,1):
        resultado=tabla*num
        print(tabla,"*", num, " = ", resultado,"\n")
        
print("Fin del ciclo.")
        
# \ ---> alt + 92
#\n ----> salta una linea n de line
#\t salta 5 espacios t de tabulador
# "\n"
