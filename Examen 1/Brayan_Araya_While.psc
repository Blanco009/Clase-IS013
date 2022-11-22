Algoritmo Brayan_Araya_While
	
	escribir "Este algoritmo calcula las respuestas a ecuaciones cuadráticas."
	escribir " A cuántas ecuaciones le desea calcular respuestas? "
	leer N
	i<-1
	Repetir
		escribir "Digite los valores para a, b y c: "
		leer a, b, c

		disc<- b*b-4*a*c
		si disc<0 entonces
			escribir "No tiene solución"
		sino
			si disc = 0 entonces
				escribir "Tiene una solución"
				x<--b /(2*a)
				escribir "La solución es: ", x
			sino 
				
				x1<-(-b+rc(disc))/(2*a)
				x2<-(-b-rc(disc))/(2*a)
				escribir "El resultado del discriminante es: ", disc
				escribir "X1= ", x1
				escribir "X2= ", x2
			fin si	
		fin si
		
		
	Hasta Que i>N
	
FinAlgoritmo
