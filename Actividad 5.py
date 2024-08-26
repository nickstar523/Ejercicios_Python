# Ingresar la edad y el sexo de la persona
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (femenino/masculino): ").lower()

# Calcular el número de pulsaciones según el sexo
if sexo == "femenino":
    pulsaciones = (220 - edad) / 10
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = 0
    print("Sexo no válido")

# Mostrar resultado
print("Número de pulsaciones por cada 10 segundos de ejercicio aeróbico: ", pulsaciones)