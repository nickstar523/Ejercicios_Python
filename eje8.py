def determinar_anemia(edad, sexo, hemoglobina):
    # Determinar el rango de hemoglobina basado en la edad y el sexo
    if edad <= 1/12:  # 0 - 1 mes
        rango_min, rango_max = 13, 26
    elif 1/12 < edad <= 6/12:  # >1y <=6 meses
        rango_min, rango_max = 10, 18
    elif 6/12 < edad <= 12/12:  # >6y <=12 meses
        rango_min, rango_max = 11, 15
    elif 1 < edad <= 5:  # >1y <=5 años
        rango_min, rango_max = 11.5, 15
    elif 5 < edad <= 10:  # >5y <=10 años
        rango_min, rango_max = 12.6, 15.5
    elif 10 < edad <= 15:  # >10y <=15 años
        rango_min, rango_max = 13, 15.5
    elif edad > 15 and sexo == "mujer":  # Mujeres >15 años
        rango_min, rango_max = 12, 16
    elif edad > 15 and sexo == "hombre":  # Hombres >15 años
        rango_min, rango_max = 14, 18
    else:
        return "Edad o sexo no válidos para el diagnóstico."

    # Determinar si el nivel de hemoglobina está dentro del rango
    if hemoglobina < rango_min:
        return "Positivo para anemia"
    else:
        return "Negativo para anemia"

# Solicitar información del usuario
edad = float(input("Ingrese la edad en años (puede usar decimales para meses): "))
sexo = input("Ingrese el sexo (mujer/hombre): ").strip().lower()
hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

# Determinar y mostrar el resultado
resultado = determinar_anemia(edad, sexo, hemoglobina)
print(f"\nResultado del análisis: {resultado}")
