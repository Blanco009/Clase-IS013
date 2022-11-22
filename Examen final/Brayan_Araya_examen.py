#Examen final Brayan Araya Rojas
#Haga un programa en Python que sea amigable que calcule el salario de N empleados .

print("Este programa calcula el salario de empleados.","\n")

n = int(input("A cuántos empleados le desea calcular el salario?: "))

for i in range(1,n + 1,1):
    empleado = input(f"Cuál es el nombre completo del empleado #{i}: ")
    horas_trabajadas = int(input("Dame el número de horas trabajadas: "))
    ausencias = int(input("Digite el número de ausencias: "))
    print("\n")
    horas_normales = 40
    horas_extras = horas_trabajadas - 40

    
    if (horas_trabajadas <= 40):
        horas_extras = 0
        salario_horas_extra =0
        salario_base = horas_trabajadas * 5000
    


    
    elif (horas_trabajadas >= 41 and horas_trabajadas <=50):
        salario_horas_extra = horas_extras * 5500
        salario_base= (horas_trabajadas - horas_extras)*5000
    

    else:
        horas_extras = 10
        salario_horas_extra = horas_extras * 5500
        salario_base = horas_normales * 5000
   
        print(empleado,"su salario es de",salario_base,"y sus horas extras máximas son",salario_horas_extra,"pero las horas extras que superan las 50 horas, no se pagan.")



        
    if (ausencias == 0):
        gratificacion = salario_base *0.03
    
    elif (ausencias >=1 and ausencias <=9):
        gratificacion = salario_base *0.02
    
    
    elif (ausencias >= 10 and ausencias <= 15):
        gratificacion = salario_base *0.01
        
    else:
        gratificacion = 0
        

    salario_bruto = salario_base + salario_horas_extra + gratificacion


    impuesto_renta = salario_bruto * 0.15


    impuesto_social = salario_bruto * 0.09


    deduciones = impuesto_renta + impuesto_social


    salario_neto = salario_bruto - deduciones

    print("\n")
    print(" El empleado",empleado,"\n","Tiene un salario base de",salario_base,"\n","Su salario por horas extras es de",salario_horas_extra,"\n","Tiene una gratificación de",gratificacion,"\n","Un salario bruto de",salario_bruto,"\n","Con un total de deducciones de",deduciones,"\n","Su salario neto es:",salario_neto,"\n")
print("\n")
print("Fin del Programa.")
