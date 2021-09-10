from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []
jogadores["Jogador 1"] = randint(1, 6)
jogadores["Jogador 2"] = randint(1, 6)
jogadores["Jogador 3"] = randint(1, 6)
jogadores["Jogador 4"] = randint(1, 6)
print("Valores sorteados:")
for i, v in jogadores.items():
    print(f"{i} tirou {v} no dado.")
    sleep(1)
print("-="*20)
print("==RANKING DOS JOGADORES==")
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)  # 1: ordena por valor(ex:randint(1, 6))/ 2: organiza por chaves(ex:jogadores["Jogador 1"])
for i, v in enumerate(ranking):
    print(f"  {i+1}° lugar: {v[0]} com {v[1]}.")  # v[0]: jogadores / v[1]: valores
    sleep(1)

