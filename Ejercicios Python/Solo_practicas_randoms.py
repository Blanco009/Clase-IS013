#solicita información del empleado.

nombre = input("Cuál es el nombre del empleado: ")
horas_trabajadas = int(input("Número de horas trabajadas: "))
ausencias = int(input("Número de ausencias?: "))


if (horas_trabajadas <=40):
    salario = (horas_trabajadas * 5000)
    print(nombre,"su salario es de ", salario)

elif (horas_trabajadas >= 41 and horas_trabajadas <= 50):

    salario_base = (40 * 5000)
    horas_extras = (horas_trabajadas - 40)
    salario_horas_extras = (horas_extras * 5500)
    
    print(nombre,"su salario es de ", salario_base," además su salario por horas extras es de ", salario_horas_extras)
    
else:
    salario_base = (40 * 5000)
    salario_horas_maximas = (10 * 5500)
    print(nombre,"su salario es de ", salario_base," además su salario por horas extras es de ", salario_horas_maximas)


print("Fin del algoritmo.")
