#se pone cualquier salario pues lo importante es hacer la retenciony bonificacion
salario = 1500000
#Ahora hacemos la retencion que es por el 18% sobre el salario
retencion = float(salario * 0.18)
# bonificacion del 1.3% sobre el salario 
bonificacion = float(salario * 0.013)
# El total seria el salario menos el valor acumulado en la retencion mas la bonificacion de la variable bonificacion y listo
total = (salario - retencion + bonificacion)
print(f"Su salario es de {salario:,}, se le aplicó la retencion del 18% y quedo: {retencion:,} ya con su bonificacion queda: {bonificacion} para un salario neto de: {total:,}")