def calcular_nota_definitiva(taller1, taller2, eval1, eval2, eval3, trabajo_final, quiz1, quiz2, quiz3, quiz4):
    nota1 = (taller1 + taller2) / 2
    nota2 = (eval1 + eval2 + eval3) / 3
    nota3 = trabajo_final
    nota4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4

    nota_definitiva = (nota1 * 0.15) + (nota2 * 0.30) + (nota3 * 0.30) + (nota4 * 0.25)
    return nota_definitiva


taller1 = float(input("Ingrese la nota del taller 1: "))
taller2 = float(input("Ingrese la nota del taller 2: "))
eval1 = float(input("Ingrese la nota de la evaluación 1: "))
eval2 = float(input("Ingrese la nota de la evaluación 2: "))
eval3 = float(input("Ingrese la nota de la evaluación 3: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))
quiz1 = float(input("Ingrese la nota del quiz 1: "))
quiz2 = float(input("Ingrese la nota del quiz 2: "))
quiz3 = float(input("Ingrese la nota del quiz 3: "))
quiz4 = float(input("Ingrese la nota del quiz 4: "))

nota_final = calcular_nota_definitiva(taller1, taller2, eval1, eval2, eval3, trabajo_final, quiz1, quiz2, quiz3, quiz4)
print(f"La nota definitiva del estudiante es: {nota_final:.2f}")
