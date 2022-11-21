#Leer un numero n y usarlo con ciclo for



x = int(input("Para cuántos alumnos desea calcular las notas?: "))



for i in range(1,x + 1 ,1):
    nombre = input(f"Dame el nombre del estudiante #{i}: ")
    print("Dame las notas en porcentajes!")
    ex1 = int(input("Nota I examen de 20%:"))
    if ex1 <= 0 or ex1 >20:
        print("Dato no válido, vuelve a intentar...")
        ex1 = int(input("Nota I examen de 20%:"))
    elif:
        ex2 = int(input("Nota II examen de 40%:"))
        if ex2 <= 0 or ex2 > 40:
            print("Dato no válido, vuelve a intentar...")
            ex2 = int(input("Nota II examen de 40%:"))
        elif:
            proy = int(input("Nota proyecto de 30%:"))
            if proy <=0 or proy > 30:
                print("Dato no válido, vuelve a intentar...")
                proy = int(input("Nota proyecto de 30%:"))
            elif:
                tarea = int(input("Nota Tareas de 10%:"))
                if tarea <= 0 or tarea > 10:
    
                    print("Dato no válido, vuelve a intentar...")
                    tarea = int(input("Nota Tareas de 10%:"))
                else:
                    nota = ex1 + ex2 + proy + tarea
                    print("El estudiante ",nombre,"tiene una nota de",nota)
                    print("************************************************")
    
    
    
print("Fin del programa")
    
