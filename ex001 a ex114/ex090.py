dados = {}

dados["nome"] = str(input("Digite seu nome: "))
dados["media"] = float(input("Digite sua media: "))
print("-="*12)
print("O nome do aluno:", dados["nome"])
print("Media:", dados["media"])
if dados["media"] >= 7:
    dados["situação"] = "Situação: Aprovado"
    print(dados["situação"])
else:
    dados["situação"] = "Situação: Reprovado"
    print(dados["situação"])