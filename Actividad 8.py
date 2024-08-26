# Ingresar los datos del paciente
edad = float(input("Ingrese la edad del paciente (en años): "))
sexo = input("Ingrese el sexo del paciente (femenino/masculino): ").lower()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina del paciente (en g%): "))

# Determinar el rango de hemoglobina adecuado según edad y sexo
if edad <= 1/12:  # 0 - 1 mes
    rango_min = 13
    rango_max = 26
elif 1/12 < edad <= 0.5:  # > 1 mes y <= 6 meses
    rango_min = 10
    rango_max = 18
elif 0.5 < edad <= 1:  # > 6 meses y <= 12 meses
    rango_min = 11
    rango_max = 15
elif 1 < edad <= 5:  # > 1 año y <= 5 años
    rango_min = 11.5
    rango_max = 15
elif 5 < edad <= 10:  # > 5 años y <= 10 años
    rango_min = 12.6
    rango_max = 15.5
elif 10 < edad <= 15:  # > 10 años y <= 15 años
    rango_min = 13
    rango_max = 15.5
else:  # > 15 años
    if sexo == "femenino":
        rango_min = 12
        rango_max = 16
    elif sexo == "masculino":
        rango_min = 14
        rango_max = 18
    else:
        print("Sexo no válido")
        rango_min = rango_max = None

# Determinar si tiene anemia o no
if rango_min is not None and rango_max is not None:
    if nivel_hemoglobina < rango_min:
        resultado = "positivo (tiene anemia)"
    else:
        resultado = "negativo (no tiene anemia)"

    # Mostrar el resultado
    print(f"El nivel de hemoglobina es {nivel_hemoglobina} g%.")
    print(f"El rango adecuado es de {rango_min} a {rango_max} g%.")
    print(f"El resultado es {resultado}.")
else:
    print("No se pudo determinar el rango de hemoglobina debido a un error en los datos.")