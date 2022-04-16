#Concatenacion
cadena1="Hola"
cadena2="Mundo"
cadenaUnida=cadena1 +" "+ cadena2
print(cadenaUnida)
cadenaRepetida=cadena1*3
print(cadenaRepetida)
#Las cadenas pueden tratarse como listas
cadena="Hola Ejemplo de cadena"
#H o l a E j e m p l  o  d   e c  a  d  e  n  a 
#1 2 3 4 5 6 7 8 9 10 11 12  13 14 15 16 17 18 19
letra = cadena[5]
print(letra)
letra = cadena[-8]
print(letra)
letra = cadena[:2]
print(letra)
modificada=cadena.capitalize()
print(modificada)
modificada = cadena.lower()
print(modificada)
modificada = cadena.upper()
print(modificada)
modificada = cadena.lower().islower()
print(modificada)
#FUNCIONES DE LAS CADENAS DE TEXTO
modificada = cadena.split()
print(modificada)
print(modificada)