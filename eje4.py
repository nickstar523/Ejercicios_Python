import random

# Solicitar el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: $"))

# Simular la elección de color de la balota
colores = ["rojo", "verde", "azul", "amarillo"]  # Colores posibles
color_balota = random.choice(colores)

# Inicializar variables para el descuento y el monto a pagar
descuento = 0
valor_a_pagar = monto_total

# Determinar el descuento basado en el color de la balota
if color_balota == "rojo":
    descuento = 0.15  # 15% de descuento
elif color_balota == "verde":
    descuento = 0.20  # 20% de descuento

# Calcular el monto a pagar después del descuento
valor_a_pagar -= monto_total * descuento

# Mostrar los resultados
print("\nDetalles de la compra:")
print(f"Monto total de la compra: ${monto_total:.2f}")
print(f"Color de la balota: {color_balota}")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Valor a pagar: ${valor_a_pagar:.2f}")
