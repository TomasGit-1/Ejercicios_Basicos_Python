def generarPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista
def generarPar(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

#print(generarPares(10))

devuelvePar=generarPar(10)
#for i in devuelvePar:
#Obtiene el primer valor
print(next(devuelvePar))
print(next(devuelvePar))
print(next(devuelvePar))
