def calcular_costo_llamada(duracion, costo_por_minuto):
    return duracion * costo_por_minuto

# Datos de las llamadas (duración en minutos)
llamadas_operador1 = [5, 3]  # dos llamadas al primer operador
llamadas_operador2 = [4, 6]  # dos llamadas al segundo operador

# Costos por minuto de cada operador
costo_por_minuto_operador1 = 2.5
costo_por_minuto_operador2 = 3.0

# Calcular costos de llamadas al operador 1
costos_operador1 = [calcular_costo_llamada(duracion, costo_por_minuto_operador1) for duracion in llamadas_operador1]
total_operador1 = sum(costos_operador1)

# Calcular costos de llamadas al operador 2
costos_operador2 = [calcular_costo_llamada(duracion, costo_por_minuto_operador2) for duracion in llamadas_operador2]
total_operador2 = sum(costos_operador2)

# Costo total de las cuatro llamadas
total_llamadas = total_operador1 + total_operador2

# Mostrar resultados
for i, costo in enumerate(costos_operador1, 1):
    print(f"Costo llamada {i} al operador 1: ${costo:.2f}")
for i, costo in enumerate(costos_operador2, 1):
    print(f"Costo llamada {i} al operador 2: ${costo:.2f}")

print(f"Costo total llamadas al operador 1: ${total_operador1:.2f}")
print(f"Costo total llamadas al operador 2: ${total_operador2:.2f}")
print(f"Costo total de las cuatro llamadas: ${total_llamadas:.2f}")
