from datetime import date

dados = {}
dados["nome"] = str(input("Nome: "))
ano_nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
dados["idade"] = ano_atual - ano_nasc
dados["ctps"] = int(input("Carteira de trabalho (0 se não tem): "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de contratação: "))
    dados["salario"] = int(input("Salario: "))
    dados["aposentadoria"] = (dados["contratação"] - ano_nasc) + 35
print("-="*20)
for i, v in dados.items():
    print(f"{i}: {v}")