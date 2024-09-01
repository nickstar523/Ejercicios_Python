# Solicitar la edad y el sexo del usuario
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (femenino/masculino): ").strip().lower()

# Inicializar la variable para el número de pulsaciones
num_pulsaciones = 0

# Determinar el número de pulsaciones basado en el sexo
if sexo == "femenino":
    num_pulsaciones = (220 - edad) / 10
elif sexo == "masculino":
    num_pulsaciones = (210 - edad) / 10
else:
    print("Sexo no válido. Por favor, ingrese 'femenino' o 'masculino'.")
    exit()  # Termina el programa si el sexo no es válido

# Mostrar el resultado
print(f"\nNúmero de pulsaciones recomendadas por cada 10 segundos de ejercicio: {num_pulsaciones:.2f}")