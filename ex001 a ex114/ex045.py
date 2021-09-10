from random import choice
from time import sleep

print("-="*10)
print("      JOKEMPÔ")
print("-="*10)
jogador = str(input("Escolha entre pedra, papel ou tesoura: ")).lower()
print("  JO")
sleep(1)
print("  KEM")
sleep(1)
print("  PÔ...")
lista = ["pedra", "papel", "tesoura"]
computador = choice(lista)
print(computador)
if computador == "pedra":
    if jogador == "pedra":
        print("Empatamos! Vamos tentar mais uma rodada!")
    elif jogador == "papel":
        print("Você ganhou!")
    elif jogador == "tesoura":
        print("Computador ganhou!")
    else:
        print("Jogada Invalida!")
elif computador == "tesoura":
    if jogador == "pedra":
        print("Você ganhou!")
    elif jogador == "papel":
        print("Computador ganhou!")
    elif jogador == "tesoura":
        print("Empatamos! Vamos tentar mais uma rodada!")
    else:
        print("Jogada Invalida!")
elif computador == "papel":
    if jogador == "pedra":
        print("Computador ganhou!")
    elif jogador == "papel":
        print("Empatamos! Vamos tentar mais uma rodada!")
    elif jogador == "tesoura":
        print("Você ganhou!")
    else:
        print("Jogada Invalida!")
