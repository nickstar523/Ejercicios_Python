# Ejercicio 5
# Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
# compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
# compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
# de la compra el valor del descuento y el valor final a pagar. 

producto = (input ("Ingresa el nombre del producto"))
cantidad = int (input("Ingresa la cantidad"))
valor = float (input("Ingresa el el valor del producto"))
descuento = float (input("Ingresa el descuento"))

valor_total = (valor - descuento)

print ("El valor total a pagar:", valor_total)

