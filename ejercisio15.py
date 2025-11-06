def sistema_liquidacion():
    inicio = int(input("Ingrese el número inicial de la registradora: "))
    fin = int(input("Ingrese el número final de la registradora: "))
    valor_pasaje = float(input("Ingrese el valor del pasaje: "))

    pasajeros = fin - inicio
    total_recaudado = pasajeros * valor_pasaje
    empresa = total_recaudado * 3 / 4
    conductor = total_recaudado - empresa

    print(f"Total de pasajeros transportados: {pasajeros}")
    print(f"Valor liquidado al conductor: {conductor:.2f}")
    print(f"Total liquidado a la empresa: {empresa:.2f}")

sistema_liquidacion()
