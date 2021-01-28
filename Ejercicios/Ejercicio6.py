numFilas,numColumn=9,11
#Ciclo for para las filas
for i in range(numFilas):
    #Ciclo for para las columnas
    for j in range(numColumn):
        #Obtenemos solo las filas 0,4,8 con el modulo
        #Pintamos la primera y ultima fila
        if i%4==0 or (j==0 or j==numColumn-1) or ((i+j)%2==0 and i%2!=0 and j==5):
            print(" * ",end="")
        else:
            print("   ",end="")
    print("")