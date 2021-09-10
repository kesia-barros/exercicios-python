resp = maior_18 = masc = menor_20 = 0
while True:
    idade = int(input("Informe a sua idade: "))
    sexo = " "
    while sexo not in "mf":
        sexo = str(input("Informe o seu sexo [M/F]")).strip().lower()[0]
    if idade > 18:
        maior_18 += 1
    if sexo == "m":
        masc += 1
    if sexo == "f" and idade < 20:
        menor_20 += 1
    resp = " "
    while resp not in "sn":
        resp = str(input("Quer continuar? [S/N]")).strip().lower()[0]
    if resp == "n":
        break
print(f"{maior_18} pessoas tem mais de 18 anos")
print(f"Tem {masc} pessoas do sexo masculino.")
print(f"Tem {menor_20} mulheres com idade menor que 20 anos.")
