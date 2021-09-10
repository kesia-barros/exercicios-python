from datetime import date

atual = date.today().year
ano_nasc = int(input("Qual o ano do seu nascimento? "))
idade = atual - ano_nasc
print("Tem {} anos de idade!".format(idade))
if idade <= 9:
    print("Faz parte da categoria MIRIM!")
elif idade > 9 and idade <= 14:
    print("Faz parte da categoria INFANTIL!")
elif idade > 14 and idade <= 19:
    print("Faz parte da categoria JÚNIOR!")
elif idade > 19 and idade <= 25:
    print("Faz parte da categoria SÊNIOR!")
else:
    print("Faz parte da categoria MASTER!")

# outra forma de fazer:

if idade <= 9:
    print("Faz parte da categoria MIRIM!")
elif idade <= 14:
    print("Faz parte da categoria INFANTIL!")
elif  idade <= 19:
    print("Faz parte da categoria JÚNIOR!")
elif  idade <= 25:
    print("Faz parte da categoria SÊNIOR!")
else:
    print("Faz parte da categoria MASTER!")
