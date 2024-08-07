# Ejercicio 4
# Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
# comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
# vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
# de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
# nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.

vendedor = (input ("Ingresa el nombre del vendedor"))
sueldo = float (input("Ingresa el sueldo del vendedor"))
comision = float (input("Ingresa la comision que recibió el vendedor"))

sueldo_total = sueldo + comision

print("El sueldo total del vendedor es :", sueldo_total)