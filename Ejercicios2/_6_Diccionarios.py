#Es una estructura de datos que nos permite alamcenar valores diferentes tipo
#(Enteros ,cadenas de texto, decimales) e incluso listas y otros diccionarios 
#clave:Valor
miDicconario={"Alemania":"Berlin", "Francia":"Paris"}
print(miDicconario["Francia"])
#Agregar un nuevo elemento 
miDicconario["Italia"]="Lisboa"
print(miDicconario)
miDicconario["Italia"]="Hola"
print(miDicconario)
#Eliminar un elemento
del miDicconario["Francia"]
print(miDicconario)
#Datos que acepta
miDicconario2={23:"Nombre","OtraClave":12}
#Mi Tupla
miTupla=("España","Francia","Reino","Alemnaia")
miDicconario4={miTupla[0]:"Madrid",miTupla[1]:"Paris"}
print(miDicconario4)
#Diccionario con tupla
miDin={23:"Jorda","Anillos":[1991,1992,1993,1994]}
print(miDin)
print(miDin["Anillos"]  )


