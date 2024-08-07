# Ejercicio 2
# Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
# La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
# algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
# del rectángulo es: yyyy
# Nota: Se debe consultar la fórmula para hallar el perímetro y el área de un rectángulo.

base=int (input ("Ingresa el tamaño de la base del rectangulo"))
altura=int (input ("Ingresa la altura del rectangulo"))
perimetro= base + altura
area= base * altura

print("El perimetro del rectangulo es:", perimetro, "El area del perimetro es:", area )