# Aumento de salarios
n = int(input("A cuántos jugadores les desea calcular el aumento de salarios?: "))
for i in range(1,n+1,1):

    nombre = input(f"Cuál es tu nombre del jugador {i}?: ")
    salario_actual = int(input("Cuál es tu salario?: "))

    while (salario_actual <= -1):
        print("Eror, el dato ingresado tiene que ser superior o igual a cero. Vuelva a ingresar un dato correcto.","\n")
        salario_actual = int(input("Cuál es tu salario?: "))
        


    if (salario_actual >=0 and salario_actual <= 500000):
        aumento = int(salario_actual * 0.20)
        nuevo_salario = salario_actual + aumento
        print("\n")
        print("Estimado Sr. "+ nombre + " por su desempeño, se le premia aumentando su salario en",aumento,".","Su salario pasa de",salario_actual,"colones a",nuevo_salario,"colones. Felicidades y gracias por ser parte de los ASTROS.","\n")

    elif (salario_actual >= 500001 and salario_actual <= 600000):
        aumento = int(salario_actual * 0.10)
        nuevo_salario = salario_actual + aumento
        print("\n")
        print("Estimado Sr. "+ nombre + " por su desempeño, se le premia aumentando su salario en",aumento,".","Su salario pasa de",salario_actual,"colones a",nuevo_salario,"colones. Felicidades y gracias por ser parte de los ASTROS.","\n")

    elif (salario_actual >= 600001 and salario_actual <= 700000):
        aumento = int(salario_actual * 0.05)
        nuevo_salario = salario_actual + aumento
        print("\n")
        print("Estimado Sr. "+ nombre + " por su desempeño, se le premia aumentando su salario en",aumento,".","Su salario pasa de",salario_actual,"colones a",nuevo_salario,"colones. Felicidades y gracias por ser parte de los ASTROS.","\n")
    else:
        print("Estimado Sr. ", nombre ,"Su salario es de",salario_actual,"colones. No hay ningún aumento. Gracias por ser parte de los ASTROS.","\n")

print("*************************************")
print("* Fin de la lista de los jugadores. *")
print("*************************************")
