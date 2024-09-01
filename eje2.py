#se pide al usuario ingresar datos

zapatillas=int(input("Ingresa la cantidad de zapatillas que desea comprar: "))
valorZapatillas= int(input("Valor de las zapatillas "))

#se realizar el procedimiento para obtener el total
total= valorZapatillas*zapatillas

#se escoge entre los descuentos dependiendo de la cantidad 
if zapatillas>=3:
    descuento=0.20
else:
    descuento=0.10

#se da un valor total a pagar incluido el descuento
valorPagar=valorZapatillas*descuento

#se da un valor total a pagar sin descuento
valor_Pagar=total-valorPagar

#finalmente se imprime una opcion dependendiendo de todo lo anterior
print(f"el valor total sin descuento seria:", total)
print(f"el valor a pagar con descuento es:", valor_Pagar)