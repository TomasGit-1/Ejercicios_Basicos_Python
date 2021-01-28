def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Reprobado"
    return valoracion
print("Programa de evalucion de notas de alumnos")
notaAlumno=int(input())
print(evaluacion(notaAlumno))
