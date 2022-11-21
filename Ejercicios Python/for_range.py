
#imprima los pares desde el cero hasta el n

#n=int(input("Hasta que número desea llegar?: ") )

#for i in range(0,n,1): #minimo, máximo, paso en paso, pero al máximo siempre se le resta 1
    #if(i%2==0): #si el residuo es 0 es para y el impar es 1

        #print(i)


#lea 3 números e imprime la suma ded ellos





suma=0
for i in range(0,3,1):
    num=int(input("Digite un número: "))
    suma=suma+num
    print("Hasta ahora la suma va dando: ",suma)
    
print(f"El resultado final es {suma}")
