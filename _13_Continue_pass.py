#Instruccion Continue
for i in "Python":
    
    if i=="h" or i=="H":
        continue
    print(f"Viendo la letra {i}")
#Intruccion Pass
#while True:
#   pass
#Else con otroa intruccion for or while
for i in "Hola@":
    if i=="@":
        arroba=True
        break
else:
    arroba=False
print(arroba)