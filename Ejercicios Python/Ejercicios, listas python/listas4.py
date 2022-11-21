# Se define la lista con los valores
cursos = ["Programación","Base de datos","Sistemas operativos","Inglés","Contabilidad"]

#Definimos la lista de aprovados vacia

aprobado = []


# este ciclo permite leer la nota de cada curso y determinar si debe repetir la materia
for i in cursos: # i es un elemento dentro de la lista cursos

#i recorre la lista de cursos
    
    nota = (int(input("Cuál es tu nota en: " + i +"?"))) # solicita la nota y se guarda en la variable nota
    if nota >=70:
        aprobado.append(i)#agrega la nota ingresada por el usuario a la lista vacia de calificaciones
##    print(calificaciones)
    



#este ciclo permite recorrer las listas para la impresion solicitada
        
#recorre la lista de aprovados
for i in aprobado:
    cursos.remove(i)
print("Tienes que repetir "+ str(cursos))
