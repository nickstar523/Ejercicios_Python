# Solicitar la cantidad de llantas compradas
cantidad_llantas = int(input("Ingrese la cantidad de llantas compradas: "))

# Definir los precios según la cantidad de llantas
precio_por_llanta = 0

if cantidad_llantas < 5:
    precio_por_llanta = 300000
elif 5 <= cantidad_llantas <= 10:
    precio_por_llanta = 250000
else:
    precio_por_llanta = 200000

# Calcular el monto total a pagar
monto_total = cantidad_llantas * precio_por_llanta

# Mostrar el resultado
print(f"\nPrecio por llanta: ${precio_por_llanta:.2f}")
print(f"Cantidad de llantas: {cantidad_llantas}")
print(f"Monto total a pagar: ${monto_total:.2f}")
