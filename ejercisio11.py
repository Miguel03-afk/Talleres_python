print ("===testamento")
herencia = float(input("Ingresa el valor de la herencia: "))

porce_esposa =  40
porce_primerhijo = 30
porce_segundohijo = 20
porce_tercerhijo = 40
porce_cuartohijo = 10

esposa = herencia * porce_esposa / 100
primer_hijo = herencia * porce_primerhijo / 100
segundo_hijo = herencia * porce_segundohijo / 100
tercer_hijo = herencia * porce_tercerhijo / 100
cuarto_hijo = herencia * porce_cuartohijo / 100

print (f"esposa: ${esposa: .2f}")
print (f"primer hijo: ${primer_hijo: .2f}")
print (f"segundo hijo: ${segundo_hijo: .2f}")
print (f"tercer hijo: $ {tercer_hijo: .2f}")
print (f"cuarto hijo: $ {cuarto_hijo: .2f}")

total = esposa + primer_hijo + segundo_hijo + tercer_hijo + cuarto_hijo

print(f"total distribucion herencia: ${total: .2f}")
