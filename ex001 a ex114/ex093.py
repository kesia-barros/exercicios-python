dados = {}
gols = []
cont = 0
dados["nome"] = str(input("Nome do Jogador: "))
partidas = int(input("Quantas partidas ele jogou: "))
for i in range(1, partidas+1):
    dados["gols"] = gols
    gols.append(int(input(f"Quantos gols na partida {i}? ")))
print("-="*30)
for gol in gols:
    cont += gol
dados["total"] = cont
print(dados)
print("-="*30)
for i, v in dados.items():
    print(f"{i}: {v}")
print("-="*30)
print(f"O jogador jogou {partidas} partidas.")
for p, v in enumerate(gols):
    print(f"  => Na partida {p+1}, fez {v} gols.")
print(f"Foi um total de {cont} gols")