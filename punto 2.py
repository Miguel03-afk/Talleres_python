
# ingresamos cualquier area ya que no se nos especifica cual era su area inicial en el input
area_inicial = float(input("Ingrese el área inicial de la cancha en metros cuadrados: "))
# creamos otra variable para almacenar el aumento sobre el area inicial puesta anteriormente y la multiplicamos por el 20%
aumento = area_inicial * 0.20
#nuevamente tomamos el area inicial para sumarla con el valor guardado en el aumento
area_total = area_inicial + aumento
print("El area total de la cancha con ampliacion es de:", area_total, "metros cuadrados")2
