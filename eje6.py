# Solicitar el promedio y la pensión base del alumno
promedio = float(input("Ingrese el promedio obtenido por el alumno: "))
pension_base = float(input("Ingrese el monto de la pensión base: $"))

# Inicializar la variable para el monto a pagar
monto_a_pagar = 0

# Determinar el monto a pagar basado en el promedio
if promedio >= 4.0:
    # Aplicar un descuento del 30% sobre la pensión base
    descuento = 0.30
    monto_a_pagar = pension_base * (1 - descuento)
else:
    # Calcular el monto a pagar incluyendo el 10% de IVA
    iva = 0.10
    monto_a_pagar = pension_base * (1 + iva)

# Mostrar el resultado
print(f"\nMonto a pagar por el alumno: ${monto_a_pagar:.2f}")
