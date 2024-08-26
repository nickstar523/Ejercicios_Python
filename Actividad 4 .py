import random

# Ingresar el valor de la compra
valor_compra = float(input("Ingrese el valor de la compra: "))

# Seleccionar un color al azar
colores = ["rojo", "verde", "otro"]
color_elegido = random.choice(colores)

# Determinar el descuento basado en el color elegido
if color_elegido == "rojo":
    descuento = 0.15 * valor_compra
elif color_elegido == "verde":
    descuento = 0.20 * valor_compra
else:
    descuento = 0.0

# Calcular el total a pagar
total_pagar = valor_compra - descuento

# Mostrar resultados
print("Valor de la compra: $", valor_compra)
print("Color de la balota: ", color_elegido)
print("Descuento aplicado: $", descuento)
print("Total a pagar: $", total_pagar)