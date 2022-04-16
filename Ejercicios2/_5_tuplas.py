#Las tuplas son unmutables es quiere decir que no se pueden modificar despues de su creacion
#Sintaxis de la tuplas
#nombreTupla=(elem1,elem2,elem3)
miTupla=(1,"Hola",4.5,False)
print(miTupla)
print(miTupla[2])
#Convertir Tupla a lista o viceversa
miLista=list(miTupla)
print(miLista)
miTupla2=tuple(miLista)
print(miTupla2)
#Encontrar un valor en una tupla
print("Hola" in miTupla)
#Contar
print(miTupla.count(1))
#Tamaño de la tupla
print(len(miTupla))
#Otra forma de generar un tupla  Empaquetado de tupla
miTupla3="Juan",13,1,1998
print(miTupla3)
#Desempaquetado de tupla
nombre,dia,mes,anio=miTupla3