def Fun_Coincidencia(palNum1,palNum2):
    palNum1=palNum1.lower()
    palNum2=list(palNum2.lower())
    posPal,contCoin,listaCoin=0,False,[]
    #While para recorrer la primera letra
    while posPal<len(palNum1):
        #Posicion de la coincidencia
        for i in range(len(palNum2)):
            #Verifico si el caracter se encunetra en mi lista
            if palNum1[posPal] in palNum2:
                if palNum1[posPal]==palNum2[i]:
                    #print(f"Coincidencia  {palNum1[posPal]} == {i} en posicion ")
                    #Modifico la lista para eliminar las coincidencias anteriores de una letra
                    listaCoin.append(i)
                    palNum2.remove(palNum2[i])
                    palNum2.insert(i,"")
                    contCoin=listaCoin
                    break
            else:
                contCoin=False
                break
        posPal+=1
    return contCoin
#Lectura de datos
palNum1=input("Ingrese el primero String ")
palNum2=input("Ingrese el segundo string ")
resultado=Fun_Coincidencia(palNum1,palNum2)
if resultado==False:
    print(f"El resultado es: {resultado}")
else:
    print(f"El resultado es: {resultado}")
