gastos = preço = mais_1000 = menor_preço = cont = 0
resp = "Ss"
barato = " "
while resp in "Ss":
    nome = str(input("Informe o nome do produto: ")).strip().lower()
    preço = float(input(f"Informe o preço do produto: R$"))
    cont += 1
    gastos += preço
    if preço > 1000:
        mais_1000 += 1
    if cont == 1:  # se for o primeiro produto, o menor preço passa a ser o preço.
        menor_preço = preço
        barato = nome
    else:
        if preço < menor_preço:
            menor_preço = preço
            barato = nome
    resp = str(input("Você quer continuar? [S/N] ")).strip().lower()[0]
    if resp == "n":
        break
print(f"O total de gastos da compra foi: R${gastos} reais.")
print(f"{mais_1000} produtos custam mais de R$1.000 reais.")
print(f"O produto mais barato foi {barato} e custa R${menor_preço} reais.")