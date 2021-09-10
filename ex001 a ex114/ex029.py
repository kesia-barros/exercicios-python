vel = float(input("Qual sua velocidade? "))
if vel > 80:
    multa = (vel - 80) * 7
    print("Você foi multado em {} reais!!!".format(multa))
else:
    print("Está tudo certo, dirija com cuidado!")