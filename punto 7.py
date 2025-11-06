# Pedir la cantidad de quintales al usuario
quintales = float(input("Ingrese la cantidad de quintales: "))

# los kilogramos seran tipo  (1 quintal = 100 kilogramos)
kilogramos = quintales * 100

print(f"{quintales} quintal(es) equivalen a {kilogramos} kilogramos.")
