# Programa que lee dos números y resuelve operaciones + , - , * , / , ** , // , %

#operadores

print("Este programa hace cálculos matemáticos.")
num1 = int(input("Digite un número: "))
num2 = int(input("Digite otro número: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
potencia = num1 ** num2
cociente = num1 // num2
residuo = num1 % num2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multi)
print("La división es: ", divi)
print("*********************************************************")
print(num1," elevado a ",num2, " da como resultado = ",potencia)
print("*********************************************************")
print("La potencia es: ", potencia)
print("El cociente es: ", cociente)
print("El residuo es: ", residuo)


