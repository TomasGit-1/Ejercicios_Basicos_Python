#Contruir un diagrama de flujo tal que dados los datos enteros
#A y B escriba el resultado de la siguiente expresion
# (A+B)**2/3
altura=int(input("Ingrese el valor de la altura "))
base=int(input("Ingrese el valor de la base "))
#resul=pow(2,(base*altura))/3
resul=((base*altura)**2)/3
print(f"El resultado es : {resul}")
