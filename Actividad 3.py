# Ingresar el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

# Determinar las acciones según el monto total
if monto_total > 500000:
    inversion_propia = 0.55 * monto_total
    prestamo_banco = 0.30 * monto_total
    credito_fabricante = monto_total - (inversion_propia + prestamo_banco)
else:
    inversion_propia = 0.70 * monto_total
    prestamo_banco = 0.30 * monto_total
    credito_fabricante = 0

# Si se solicita crédito al fabricante, calcular el interés
if credito_fabricante > 0:
    interes_credito = 0.20 * credito_fabricante
else:
    interes_credito = 0

# Mostrar resultados
print("Valor invertido de su propio dinero: $", inversion_propia)
print("Valor prestado al banco: $", prestamo_banco)
print("Valor del crédito solicitado al fabricante: $", credito_fabricante)
print("Interés por crédito al fabricante: $", interes_credito)