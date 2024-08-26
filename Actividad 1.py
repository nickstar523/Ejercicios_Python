# Ingresar las tres calificaciones
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Determinar si aprueba o no
if promedio >= 70:
    print("El aprendiz aprueba la asignatura con un promedio de:", promedio)
else:
    print("El aprendiz reprueba la asignatura con un promedio de:", promedio)