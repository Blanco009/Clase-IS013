
print("***************************************************************************")
print("*Este programa brinda información acerca del comercio entre varios paises.*")
print("***************************************************************************","\n")

print("********************************")
print("*DIGITE LOS DATOS DEL AÑO 2020.*")
print("********************************","\n")
#creamos dos tipos de listas para almacenar paises
importadores=["México ","Paraguay ","Venezuela "]
Exportadores=["Argentina ","Brasil ","Costa Rica "]
#Creamos tres listas para almacenar los datos de las exportaciones de 2020
Argentima=[0]*3
Brasil=[0]*3
Costa=[0]*3
#Creamos tres listas para almacenar los datos de las exportaciones de 2021
Argentima1=[0]*3
Brasil1=[0]*3     
Costa1=[0]*3

#Se crea una funcion que solicite los datos
#al usarla le indicamos en cuales listas queremos almacenar los datos
#ejemplo1: "entradaDatos(Argentima,Brasil,Costa)" para los datos del 2020
#ejemplo2: "entradaDatos(Argentima1,Brasil1,Costa1)" para los datos del 2021
#usamos un ciclo para repetir la solicitud para cada pais
#usamos las listas para almacenar los datos en campos especificos
#usamos condicionales para almacenar los datos en su pais correcto
def entradaDatos (pais0,pais1,pais2):
    for paisExp in range (0,3):
        print("--------------------------------")
        print("Cuánto exportó "+Exportadores[paisExp]+ "a: ")
        for paisImp in range (0,3):
            if paisExp==0:
                (pais0[paisImp])=int(input(importadores[paisImp]+":"))
            elif paisExp==1:
                (pais1[paisImp])=int(input(importadores[paisImp]+":"))
            elif paisExp==2:
                (pais2[paisImp])=int(input(importadores[paisImp]+":"))
        print("--------------------------------"+"\n")
#Aqui hacemos uso de la funcion creada antes, le damos los parametros para que almacenelos datos de 2020
entradaDatos(Argentima,Brasil,Costa)#le decimos que almacene los datos en las listas de exportadores Arg, brasil y Costa rica.
#almacenamos las importaciones respectivas de cada pais en 2020
mex=[Argentima[0],Brasil[0],Costa[0]]#Las listas de importaciones se crean, clasificando los datos ingresados y almacenados de las exportaciones
para=[Argentima[1],Brasil[1],Costa[1]]#que se ingresaron antes, pero en su pais correspondiente gracias a la posicion de las listas.
vene=[Argentima[2],Brasil[2],Costa[2]]#ejemplo: Argetina exportó [0=Mexico,1=Paraguay,2=Venezuela ]

print("*********************************")
print("* DIGITE LOS DATOS DEL AÑO 2021.*")#Repetimos el proceso para solicitar datos, esta vez los almacenamos en variables diferentes
print("*********************************","\n")#En variables diferentes, para poder hacer uso de los datos solicitados para 2020 y 2021
print("--------------------------------")

entradaDatos(Argentima1,Brasil1,Costa1)#usamos la funcion antes creada para ingresar datos
#PERO le indicamos que los almacene en otras variables
#almacenamos las importaciones respectivas de cada pais en 2021     
mex1=[Argentima1[0],Brasil1[0],Costa1[0]]#ejemplo: Argentina exporto [0=Mexico,1=Paraguay,2=Venezuela]
para1=[Argentima1[1],Brasil1[1],Costa1[1]]
vene1=[Argentima1[2],Brasil1[2],Costa1[2]]

cont=1 #mientras el contador este sea 1 se repite el ciclo
while cont==1: #creamos un contador para que se puedan hacer consultas repetidamente
    #Imprimimos las posibles consultas a realizar por el usuario y la informacion de los paises
    print("GRUPO 1:", str(Exportadores))
    print("GRUPO 2:", str(importadores), "\n")
    print("--------------------------------------------------------------------")
    print("1. ¿Cuánto exportó cada país del GRUPO 1 en cada año?")
    print("2. ¿Cuánto exportó cada país del GRUPO 1 en total en ambos años?")
    print("3. ¿Cuánto exportó cada país del GRUPO 1 en promedio de ambos años?","\n")
    print("4. ¿Cuánto importó cada país del GRUPO 2 en cada año?")
    print("5. ¿Cuánto importó cada país del GRUPO 2 en total en ambos años?")
    print("6. ¿Cuánto importó cada país del GRUPO 2 en promedio de ambos años?")
    print("--------------------------------------------------------------------","\n")
    #preguntamos la consulta a especifica que desea realizar
    print("_______________________________________________________________")
    select=int(input("* Digite el número de la consulta que desea realizar:"))#en esta variable almacenamos el numero equivalente ala consulta realizada
    print("_______________________________________________________________","\n")
    #sumamos totales por pais exportador en 2020
    a=sum(Argentima)#usamos la funcion sum() y almacenamos los resultados en variables especificas por pais.
    b=sum(Brasil)#ejemplo: Brasil=[1,1,1], al usar la funcion sum(brasil), suma los datos almacenados en esa lista osea 3.
    c=sum(Costa)#y los almacena en otra variable para poder responder a las consultas especificas.
    x=sum(mex)#aqui igual pero con las listas de exportaciones.
    y=sum(para)
    z=sum(vene)
    #sumamos totales por pais exportador en 2021
    a1=sum(Argentima1)#se repite el proceso anterio pero con datos del 2021
    b1=sum(Brasil1)
    c1=sum(Costa1)
    x1=sum(mex1)
    y1=sum(para1)
    z1=sum(vene1)
    #aqui creamos listas nuevas, que van a almacenar los valores de las sumas anteriores
    #esto para poder hacer uso de ciclos mas adelante.
    exp1=[a,b,c] #almacena todas las exportaciones de Argentina, brasil y costa rica de 2020
    exp2=[a1,b1,c1]#almacena los todas las exportaciones de Argentina, brasil y costa rica de 2021
    imp1=[x,y,z]#almacena todas las importaciones de mexico, paraguay y venezuela en 2020
    imp2=[x1,y1,z1]#almacena todas las importaciones de mexico, paraguay y venezuela en 2021
    
    
    #impresiones de los resultados, dependiendo de la consulta
    # w recorre 3 posiciones de una lista 
    for w in range (0,3): #se crea un ciclo para imprimir los datos de las listas antes creadas
        if select <=0 or select > 6: # si el usuario seleccione un numero menor o igual a 0 y un numero mayor a 6, se vuelve a solicitar el numero de la consulta.
                select=int(input("Error! Opción inválida. Digite el número de la consulta que desea realizar: "))
                print("----------------------------------------------------------------------------","\n")
                
            # v recorre 3 posiciones de una lista 
        for v in range (0,3): #Se crea un ciclo para imprimir las respuestas a la consulta realizada por el usuario, ya sea del 1 al 6.
            if w==v and select==1:#Si el usuario selecciona 1 
                print(Exportadores[w],"exportó un total de",exp1[v],"millones de dólares en el año 2020 y",exp2[v],"millones de dólares en el año 2021.","\n")
            elif w==v and select==2:
                print(Exportadores[w],"exportó",exp1[v]+exp2[v],"millones de dólares en ambos años.","\n")#En cada opción se utiliza las listas citadas anteriormente.
            elif w==v and select==3:
                print(Exportadores[w],"exportó un promedio de",(exp1[v]+exp2[v])/6,"millones de dólares en ambos años.","\n")
            elif w==v and select==4:
                print(importadores[w],"importó un total de",imp1[v],"millones de dólares en el año 2020 y",imp2[v],"millones de dólares en el año 2021.","\n")
            elif w==v and select==5:
                print(importadores[w],"importó",imp1[v]+imp2[v],"millones de dólares en ambos años.","\n")
            elif w==v and select==6:
                print(importadores[w],"importó un promedio de",(imp1[v]+imp2[v])/6,"millones de dólares en ambos años.","\n")
            # w recorre las listas Exportadores[w] y importadores[w].
            # v recorre las listas exp1[v] ,exp2[v] y imp1[v] , imp2[v].
        
            


    print("***************************")
    print("* Fin de la primera parte.*")
    print("***************************","\n")

#Sección del código que se encarga de procesar las comparaciones entre paises del grupo 1 y grupo 2.
#Creamos dos listas que almacenan:
    letter=["A","B","C"]#caracteres para paises exportadores (Argentina, Brasil, Costa rica)
    letter2=["X","Y","Z"]#caracteres para paises importadores (meXico, paraguaY, veneZuela)
    def letraYpais (Lista1,lista2):#se define funcion que imprima datos de paises exportadores e importadores.)
        print("------------------------------")
        if lista2==Exportadores:
            print("Paises exportadores - Grupo 1.")#dentro de la funcion, SI el parametro dado en lista2 es la lista exportadores, lo imprime.
        else: print("Paises Importadores - Grupo 2.")#si en cambio el parametro dado en la lista2 es la lista de importadores, lo imprime.
        for w in range (0,3):#usamos ciclos nuevamente para mostrar cual es la letra clave de cada pais
            print(Lista1[w],":",lista2[w])

    letraYpais(letter,Exportadores)#Se llama la función y se le asignanlos dos parámetros, las letras y la lista de los exportadores.
    print("------------------------------","\n")
    print("_____________________________________________________________")
    option=input("Digíte el país del grupo 1 que desea comparar con el grupo 2:")#esta variable almacena la opcion del grupo 1 para comparar con el grupo 2.
    print("_____________________________________________________________","\n")

    #se utilizan varios condicionales anidados, para que si el usuario ingresa un carácter en mayúscula o minúscula ambos se han aceptados.
                     
    if option==("A") or option==("a"):#si la primera opcion es (A o a): 
        option=0  #opcion es 0 porque argentina esta en la posicion 0 de la lista exportadores[0, ,]
        choose=Argentima   #esta variable va ser igual a la lista Argentima[] del 2020
        choose2=Argentima1   #esta variable va a ser igual a la lista Argentima1[]del 2021
        
    elif option==("B") or option==("b"):#si la primera opción es (B o b):
        option=1 #opción es 1 porque Brasil está en la posición 1 de la lista exportadores[0,1,]
        choose=Brasil #esta variable va ser igual a la lista Brasil[] del 2020
        choose2=Brasil1 #esta variable va ser igual a la lista Brasil1[] del 2021
        
    elif option==("C") or option==("c"):#si la primera opción es (C o c):
        option=2 #opción es 1 porque Costa está en la posición 2 de la lista exportadores[0,1,2]
        choose=Costa #esta variable va ser igual a la lista Costa[] del 2020
        choose2=Costa1 #esta variable va ser igual a la lista Costa1[] del 2021
    
        
        
        
    letraYpais(letter2,importadores)#Se llama la función y se le asignanlos dos parámetros, pero ahora se utiliza las (letras2 y la lista de los importadores).
    print("------------------------------","\n")
    print("_____________________________________________________________")            
    option2=input("Digíte el país del grupo 2 que desea comparar con el grupo 1:")
    print("_____________________________________________________________","\n")

    if option2==("X")or option2==("x"):
        option2=0     #igualamos a 0 porque mexico (X o x) esta almacenado en la posicion 0 de la lista importadores[0, , ]
        import_total=mex #esta variable va ser igual a la lista mex[] del 2020
        import_total1=mex1 #esta variable va ser igual a la lista mex1[] del 2021
        
    elif option2==("Y") or option2==("y"):#paraguay
        option2=1  #igualamos a 1 porque paraguay (Y o y) esta almacenado en la posicion 1 de la lista importadores[0,1, ]
        import_total=para #esta variable va ser igual a la lista para[] del 2020
        import_total1=para1 #esta variable va ser igual a la lista para1[] del 2021
        
    elif option2==("Z") or option2==("z"):
        option2=2 #igualamos a 2 porque mexico (Z o z) esta almacenado en la posicion 2 de la lista importadores[0,1,2]
        import_total=vene #esta variable va ser igual a la lista vene[] del 2020
        import_total1=vene1 #esta variable va ser igual a la lista vene1[] del 2021
        
   
        

   #imprimimos(el nombre del exportador, "exporto", lista de exportaciones del pais, "millones de dolares para, nombre del importad") 
    print(Exportadores[option],"exportó",choose[option2],"millones de dólares para",importadores[option2],"en el año 2020.","\n")
    print(Exportadores[option],"exportó",choose2[option2],"millones de dólares para",importadores[option2],"en el año 2021.","\n")

    #Aqui se muestra cuanto decreció o creció una exportacion.
    if choose[option2]>choose2[option2]: #decreció
        incremento=(choose[option2]-choose2[option2])
        diferencia=(incremento/choose[option2])#diferencia para porcentaje
        porcentaje=(diferencia*100)
        porcentaje1=round(porcentaje,2)
        print("Las exportaciones de ", Exportadores[option], "en el 2021 decrecieron con respecto al 2020 un: ",porcentaje1,"%","\n")
        
    elif choose[option2]<choose2[option2]: #creció
        incremento=(choose2[option2]-choose[option2])
        diferencia=(incremento/choose[option2])
        porcentaje=(diferencia*100)
        porcentaje1=round(porcentaje,2)
        print("Las exportaciones de ", Exportadores[option], "en el 2021 crecieron con respecto al 2020 un: ",porcentaje1,"%","\n")

    #Aqui se muestra el promedio de exportaciones del pais del grupo 1, al pais del grupo 2 en ambos años.
    promedio=(choose[option2]+choose2[option2])/2 #aqui se calcula el promedio de exportaciones de una pais a otro en ambos años
    print(Exportadores[option], "exportó un promedio de",promedio,"millones de dólares a ",importadores[option2], "en ambos años.","\n")
    
    #Aqui Se muestra cuanto exporto en total el pais del grupo 1 en 2020 y cuanto en 2021.
    print(Exportadores[option],"exporto un total de",sum(choose),"millones de dólares en el 2020 y",sum(choose2),"millones de dólares en el 2021.","\n")
    #aqui se muestra cuanto importó en total el pais del grupo 2 en 2020 y cuanto en 2021.
    print(importadores[option2],"importó un total de",sum(import_total),"millones de dólares en el 2020 y",sum(import_total1),"millones de dólares en el 2021.")

    print("--------------------------------------------------------------------")
    cont=int(input("¿Desea realizar otra consulta? (0)= NO   |  (1)= SI:"))
    print("--------------------------------------------------------------------","\n")
          
print("*************************")         
print("* Fin del algoritmo. =D *")
print("*************************")
