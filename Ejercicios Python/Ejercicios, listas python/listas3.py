# Se define la lista con los valores
cursos = ["Programación","Base de datos","Sistemas operativos","Inglés","Contabilidad"]

#Definimos la lista de calificaciones vacia
calificaciones = []


# este ciclo permite leer la nota de cada curso y almacenarla en la lista calificaciones
for i in cursos: # i es un elemento dentro de la lista cursos
    nota = (int(input("Cuál es tu nota en: " + i +"?"))) # solicita la nota y se guarda en la variable nota
    calificaciones.append(nota)#agrega la nota ingresada por el usuario a la lista vacia de calificaciones
##    print(calificaciones)
    


#este ciclo permite recorrer las listas para la impresion solicitada
cont = 0 # contador para "caminar" por cada indice.
for j in cursos:
    print("En" , j, "su nota es" , calificaciones[cont])# va a imprimir la nota guardada en el numero del contador
    cont += 1
