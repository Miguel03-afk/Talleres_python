
herencia_total = float(input("Ingrese el valor total de la herencia: "))


esposa = herencia_total * 0.40


restante = herencia_total * 0.60


hijo1 = restante * 0.30
hijo2 = restante * 0.20
hijo3 = restante * 0.40
hijo4 = restante * 0.10

print("\nRepartición de la herencia:")
print(f"Esposa recibe: ${esposa}")
print(f"Hijo 1 recibe: ${hijo1}")
print(f"Hijo 2 recibe: ${hijo2}")
print(f"Hijo 3 recibe: ${hijo3}")
print(f"Hijo 4 recibe: ${hijo4}")
