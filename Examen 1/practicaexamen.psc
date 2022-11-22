Algoritmo Brayan_Araya_Astrosssssss
	
	
	
	
	Escribir "Nombre del jugador ",contador
	leer nombre
	Escribir " su salario es de: "
	leer salario
	aumento<-0
		
		
	si salario >= 0 y salario <= 500000 Entonces
		aumento<-salario*0.20
		nuevo_salario<-salario+aumento
		Escribir"Estimado Sr. ",nombre," por su desempeño, se le premia aumentando su salario en ","C",aumento,". Su salario pasa de C",salario, " a ","C",nuevo_salario,"."," Felicidades y gracias por ser parte de Los Astros."
			
			
	SiNo
		si salario >= 500001 y salario <= 600000 Entonces
			aumento<-salario*0.10
			nuevo_salario<-salario+aumento
			Escribir"Estimado Sr. ",nombre," por su desempeño, se le premia aumentando su salario en ","C",aumento,". Su salario pasa de C",salario, " a ","C",nuevo_salario,"."," Felicidades y gracias por ser parte de Los Astros."
				
				
		SiNo
			si salario >= 600001 y salario <= 700000 Entonces
				aumento<-salario*0.05
				nuevo_salario<-salario+aumento
				Escribir"Estimado Sr. ",nombre," por su desempeño, se le premia aumentando su salario en ","C",aumento,". Su salario pasa de C",salario, " a ","C",nuevo_salario,"."," Felicidades y gracias por ser parte de Los Astros."
					
					
			SiNo
				Escribir "No hay aumento"
			FinSi
				
		FinSi
			
			
		FinSi
		
		
	
	
	
	
FinAlgoritmo
