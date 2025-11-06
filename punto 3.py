# No se nos da una tasa inicial así que tomamos el 100% como base
primer_tasa = 100

# ahora el aumento del 9.5% sobre la tasa inicial
segunda_tasa = float(primer_tasa * 0.095)

# despues sumamos ese aumento a la tasa inicial para obtener la nueva tasa con el incremento
tasa_con_aumento = primer_tasa + segunda_tasa

# ahora la disminución del 1.5% sobre la tasa ya aumentada
tercer_tasa = float(tasa_con_aumento * 0.015)

# por ultimo la tasa final es restando la disminución a la tasa con aumento
totaltasa = (tasa_con_aumento - tercer_tasa)


print(f"El valor de la segunda tasa: {segunda_tasa:} y la disminución fue de {tercer_tasa:,.2f}, dando una tasa actual de: {totaltasa:.2f}")
