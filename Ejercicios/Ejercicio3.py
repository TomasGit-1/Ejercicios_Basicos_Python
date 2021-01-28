#Dada la matricula y 5 calificaciones de un alumno obtenidas a lo largo del semestre
#construye un diagrama de flujo que imprima la matricula del alumno y el promedio
#de sus calificaciones
#Si queremos guardas las calificaciones esta es una opcion
#listaMat.append(int(input(f"Ingrese la calificacion de la materia numero {i}")))
listaMat,acumMat=[],0
matricula=int(input("Ingrese la matricula del alumno "))
for i in range(0,5):
    acumMat+=float(input(f"Ingrese la calificacion de la materia numero {i} "))
print(f"La matricula es:{matricula}, el promedio es: {(acumMat/5)}")