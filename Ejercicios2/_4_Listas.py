#Uso de lista
#Es una estructura de datos que nos permite almacenar gran  cantidad de valores
#En python las listas pueden guardar diferentes tipos de valores
#Se pueden expandir dinamicamente añadiendo nuevos elementos 
#Sintaxis nombreLista=[Elem1,Elem2,Elem2.....]    0,1,2
miLista=["Tomas","Lopez","Perez",78,False]
print(miLista[:])
print(miLista[2])
#Empieza a moverse alreves y empieza desde 0
print(miLista[-2])
#Porcion de lista
print(miLista[1:2])
#Agregar elementos append lo inserta al final
miLista.append("Nuevo Elemento")
print(miLista[:])
#Agregar en una posicion especifica funcion insert
miLista.insert(2,"Nuevo")
print(miLista[:])
#Agregar varios elementos a la vez extend
miLista.extend(["Un","nue","Usuario"])
print(miLista[:])
#Obtener el indice de un elemento
print(miLista.index("Perez"))
#Saber si un elemento se encuentra en una lista
print("Pepe" in miLista)
#Eliminar un elemento
miLista.remove(78)
print(miLista[:])
#Elimina el ultimo elemento de una lista
miLista.pop()
#Operaciones con listas
miLista2=[1,2]
miTotal=miLista+miLista2
#Repetir
print(miTotal*3)
