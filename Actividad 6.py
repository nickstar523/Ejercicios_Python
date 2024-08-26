# Ingresar el promedio del alumno y el valor de la pensión
promedio = float(input("Ingrese el promedio del alumno: "))
valor_pension = float(input("Ingrese el valor de la pensión: "))

# Determinar el descuento basado en el promedio
if promedio >= 4.0:
    descuento = 0.30 * valor_pension
else:
    descuento = 0.0

# Calcular el valor a pagar
valor_con_descuento = valor_pension - descuento
valor_final = valor_con_descuento + (0.10 * valor_con_descuento)  # Agregar 10% de IVA

# Mostrar resultados
print("Valor de la pensión original: $", valor_pension)
print("Descuento aplicado: $", descuento)
print("Valor a pagar con IVA incluido: $", valor_final)