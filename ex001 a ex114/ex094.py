dados = {}
lista = []
media = soma = 0
while True:
    dados["nome"] = str(input("Informe seu nome: ")).strip()
    while True:
        dados["sexo"] = str(input("Informe o seu sexo [F/M]: ")).strip().upper()[0]
        if dados["sexo"] in "MF":
            break
        print("Erro! Por favor, digite apenas M ou F.")
    dados["idade"] = int(input("Informe sua idade: "))
    lista.append(dados.copy())
    soma += dados["idade"]
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print("-="*30)
print(f"A) Ao todo {len(lista)} pessoas foram cadastradas.")
print("-="*30)
media = soma / len(lista)
print(f"B) A media de idade das pessoas cadastradas e: {media:.1f}.")
print("-="*30)
print(f"Mulheres cadastradas: ")
for i in lista:
    if i["sexo"] == "F":
        print(f"{i['nome']}")
print("-="*30)
print(f"Pessoas cadastradas com idade maior que a media:")
for i in lista:
    if i["idade"] >= media:
        print(" ")
        for k, v in i.items():
            print(f"{k} = {v}")
print("-="*30)