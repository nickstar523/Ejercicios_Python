# Solicitar el monto total de la compra
monto_Total = float(input("Ingrese el monto total de la compra: $"))

# Inicializar las variables para los diferentes tipos de financiamiento
inversion_propio_dinero = 0
prestamo_banco = 0
credito_fabricante = 0

# Determinar el financiamiento basado en el monto total
if monto_Total > 500000:
    # Calcula la inversión de su propio dinero, préstamo al banco y crédito al fabricante
    inversion_propio_dinero = monto_Total * 0.55
    prestamo_banco = monto_Total * 0.30
    credito_fabricante = monto_Total - inversion_propio_dinero - prestamo_banco
else:
    # Calcula la inversión de su propio dinero y crédito al fabricante
    inversion_propio_dinero = monto_Total * 0.70
    credito_fabricante = monto_Total - inversion_propio_dinero
    # El fabricante cobra un 20% sobre el crédito solicitado
    credito_fabricante_total = credito_fabricante * 1.20

# Mostrar los resultados
print("\nDesglose del financiamiento:")
print(f"Inversión de propio dinero: ${inversion_propio_dinero:.2f}")
print(f"Préstamo del banco: ${prestamo_banco:.2f}")
print(f"Crédito solicitado al fabricante: ${credito_fabricante:.2f}")

if monto_Total <= 500000:
    print(f"Total a pagar al fabricante (incluyendo intereses): ${credito_fabricante_total:.2f}")
