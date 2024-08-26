# Ingresar el precio de una zapatilla y la cantidad comprada
precio_zapatilla = float(input("Ingrese el precio de una zapatilla: "))
cantidad = int(input("Ingrese la cantidad de zapatillas compradas: "))

# Calcular el total de la compra
total_compra = precio_zapatilla * cantidad

# Aplicar el descuento según la cantidad comprada
if cantidad >= 3:
    descuento = 0.20 * total_compra
else:
    descuento = 0.10 * total_compra

# Calcular el total a pagar
total_pagar = total_compra - descuento

# Mostrar resultados
print("Valor de la compra: $", total_compra)
print("Valor del descuento: $", descuento)
print("Total a pagar: $", total_pagar)