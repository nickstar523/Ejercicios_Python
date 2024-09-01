#Pedir al usuario meter las notas
nota1=float(input("Ingrese la primera nota "))
nota2=float(input("Ingrese la segunda nota "))
nota3=float(input("Ingrese la tercera nota "))

#se hace el proceso de las notas para obtener el resultado
resultado=(nota1+nota2+nota3)/3

#se imprime el promedio
print("EL promedio es", resultado)

#se imprime un resultado dependiendo de la nota final
if resultado >= 3.0 :
    print("EL resultado final es","%.1f" % resultado, "el estudiante aprobo la materia")
elif resultado < 3.0 :
    print("EL resultado final es","%.1f" % resultado, "el estudiante no aprobo la materia")