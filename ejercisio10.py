print ("===registro de entrenamiento del atleta===")

tiempo1 = float(input("Tiempo del dia 1(minutos): "))
distancia1 = float(input("distancia recorrida dia 1(metros): "))

tiempo2 = float(input("Tiempo del dia 2(minutos): "))
distancia2 = float(input("distancia recorrida dia 2(metros): "))

tiempo3 = float(input("Tiempo del dia 3(minutos): "))
distancia3 = float(input("distancia recorrida dia 3(metros): "))

total_tiempo = tiempo1 + tiempo2 + tiempo3
total_distancia = distancia1 + distancia2 + distancia3

promedio_tiempo = total_tiempo / 3
promedio_distancia = total_distancia / 3

print(f"tiempo total de entrenamiento: {total_tiempo: .2f} minutos")
print(f"distancia total recorrida: {total_distancia: .2f} metros")
print(f"promedio de tiempo por dia: {promedio_tiempo: .2f} minutos")
print(f"promedio distancia por dia: {promedio_distancia: .2f} metros")
                      