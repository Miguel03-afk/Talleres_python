def calcular_baldosas():
    alto = float(input("Ingrese el alto del muro en metros: "))
    ancho = float(input("Ingrese el ancho del muro en metros: "))
    
    area = alto * ancho
    baldosas_necesarias = area / 3.5
    
    print(f"El área del muro es: {area:.2f} metros cuadrados")
    print(f"Número de cajas de baldosas necesarias: {baldosas_necesarias:.2f}")

calcular_baldosas()