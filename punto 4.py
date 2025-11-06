# Pedimos la area inicial
area_inicial = float(input("Ingresa el area inicial del terreno (en metros cuadrados): "))

# reducimos  el 10% segun el enunciado
area_reducida = area_inicial - (area_inicial * 0.10)

# aumentamos el 50% con base en el área reducida
area_final = area_reducida + (area_reducida * 0.50)

# Mostramos el resultado
print(f"El área total final del terreno es: {area_final} metros cuadrados.")
