# Ingresar la cantidad de llantas compradas
cantidad_llantas = int(input("Ingrese la cantidad de llantas compradas: "))

# Determinar el precio por llanta basado en la cantidad comprada
if cantidad_llantas < 5:
    precio_por_llanta = 300000
else:
    precio_por_llanta = 250000

# Calcular el total a pagar
total_pagar = precio_por_llanta * cantidad_llantas

# Mostrar resultado
print("Cantidad de llantas compradas:", cantidad_llantas)
print("Precio por llanta: $", precio_por_llanta)
print("Total a pagar: $", total_pagar)