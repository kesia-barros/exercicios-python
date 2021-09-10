dados = {}
gols = []
time = []
cont = 0
while True:
    dados.clear()
    dados["nome"] = str(input("Nome do Jogador: "))
    partidas = int(input("Quantas partidas ele jogou: "))
    gols.clear()
    for i in range(1, partidas+1):
        gols.append(int(input(f"Quantos gols na partida {i}? ")))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    time.append(dados.copy())
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
#cabeçalho

print("-="*30)
print("cod ", end="")
for i in dados.keys():
    print(f"{i:<15}", end="")
print()
#os campos

print("-="*30)
for k, v in enumerate(time):
    print(f"{k:>3}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("-="*30)
while True:
    busca = int(input("Mostrar dados de qual jogador? [999 para parar]: "))
    if busca == 999:
        break
    if busca >= len(time):
      print(f"ERRO! Não existe jogador com codigo {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, v in enumerate(time[busca]['gols']):
            print(f"  No jogo {i+1} fez {v} gols.")
    print("-=" * 30)
print("<< VOLTE SEMPRE >>")