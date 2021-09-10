nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média é: ", media)
if media < 5:
    print("\033[31mVocê está reprovado!!!")
elif media >= 5 and media < 6.9:
    print("\033[33mVocê está de recupeção!")
elif media == 7 or media > 7:
    print("\033[32mVocê está aprovado!")