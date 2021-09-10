from datetime import date
atual = date.today().year
ano_nasc = int(input("Qual o seu ano de nascimento?"))
idade = atual - ano_nasc
print("Você tem {} anos de idade!".format(idade))
if idade == 18:
    print("É hora de se alistar!")
elif idade > 18:
    atraso = idade - 18
    print("Passou da hora de se alistar!")
    print("Já passou {} anos do seu alistamento!".format(atraso))
else:
    aguardo = 18 - idade
    print("Faltam {} anos para você se alistar!".format(aguardo))