primer_tasa = 100
segunda_tasa = float(primer_tasa * 0.095)  
tasa_con_aumento = primer_tasa + segunda_tasa
tercer_tasa = float(tasa_con_aumento * 0.015)  
totaltasa = (tasa_con_aumento - tercer_tasa)

print(f"El valor de la segunda tasa: {segunda_tasa:} y la disminución fue de {tercer_tasa:,.2f}, dando una tasa actual de: {totaltasa:.2f}")


