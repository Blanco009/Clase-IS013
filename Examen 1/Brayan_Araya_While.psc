Algoritmo Brayan_Araya_While
	
	escribir "Este algoritmo calcula las respuestas a ecuaciones cuadr�ticas."
	escribir " A cu�ntas ecuaciones le desea calcular respuestas? "
	leer N
	i<-1
	Repetir
		escribir "Digite los valores para a, b y c: "
		leer a, b, c

		disc<- b*b-4*a*c
		si disc<0 entonces
			escribir "No tiene soluci�n"
		sino
			si disc = 0 entonces
				escribir "Tiene una soluci�n"
				x<--b /(2*a)
				escribir "La soluci�n es: ", x
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
