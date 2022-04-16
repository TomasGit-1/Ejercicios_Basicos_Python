#Creamos una funcion
def mensaje():
    print("Esta es una funcion_1")
    print("Esta es una funcion_2")
    print("Esta es una funcion_3")
    print("Esta es una funcion_4")
#Se manda a llamar la duncion
#mensaje()
def suma():
    numero1=5
    numero2=6
    print(numero1+numero2)
def sumaP(num1,num2):
    print(num1+num2)
def sumaR(num1,num2):
    resultado=num1+num2
    return resultado
#Funcion sin parametros
suma()
#Funcion con parametros
sumaP(2,4)
#Funcion con return 
print(sumaR(5,3))

