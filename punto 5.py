# pedimos la cantidad de minutos al usuario
minutos = int(input("Ingrese la cantidad de minutos: "))

# Ahora en estas 2 variables calculamos  las horas y los minutos restantes
horas = minutos // 60       # División entera para las horas
resto = minutos % 60        # usamos el modulo para obtener el resto de la division en este caso son  los minutos sobrantes

print(f"{minutos} minutos equivalen a {horas} hora(s) y {resto} minuto(s).")
