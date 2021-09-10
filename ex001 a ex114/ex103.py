def ficha(nome='desconhecido', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no compeonato.")


nome_jog = str(input("Nome do jogador: "))
gols_jog = str(input("Gols do jogador: "))
if gols_jog.isnumeric():
    gols_jog = int(gols_jog)
else:
    gols_jog = 0
if nome_jog.strip() == "":
    ficha(gols=gols_jog)
else:
    ficha(nome_jog, gols_jog)