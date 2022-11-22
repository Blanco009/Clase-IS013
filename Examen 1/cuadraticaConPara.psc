Algoritmo cuadraticawhile
	escribir "este pseudocódigo calcula las respuestas a ecuaciones cuadráticas"
	
	escribir " A cuántas ecuaciones le quiere calcular respuestas? "
	leer N
	
	Para i<-1 hasta N con paso 1 hacer
		
		escribir "digite los valores para a, b y c"
		leer a, b, c
		//calculamos el discriminante
		disc<- b*b-4*a*c
		si disc<0 entonces
			escribir "no tiene solución"
		sino
			si disc=0 entonces
				escribir "tiene una solución"
				x<- -b /(2*a)
				escribir "la solución es: ", x
			sino 
				//como disc es mayor que cero entonces calculamos x1 y x2 usando disc
				x1<- (-b + rc(disc))/(2*a)
				x2<- (-b - rc(disc))/(2*a)
				escribir "el resultado del discriminante es: ", disc
				escribir "X1= ", x1
				escribir "X2= ", x2
			fin si	
		fin si
		
	Fin Para
FinAlgoritmo
