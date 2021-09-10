sal = float(input("Qaul é o seu salário?"))
if sal <= 1250:
    aumento = (sal * 0.15) + sal
else:
    aumento = (sal * 0.10) + sal
print("Seu salario aumentou para R$ {:.3f} reais!".format(aumento))
