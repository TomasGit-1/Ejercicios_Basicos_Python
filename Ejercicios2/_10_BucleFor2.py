for i in ["Pildoras","Informatica",2]:
    print("Hola",end=" ")
for i in "TomasLopezPerez":
    print(i,end=" ")
email=False
txtEmail=input("Introduce tu direccion de email")
for i in txtEmail:
    if i=="@":
        email=True
if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")
#Uso de range
for i in range(5):
    print("Hola")