from random import randint
from time import sleep

computador = randint(0, 5)
print("Escolha um numero de 0 entre 5 ")
jogador = int(input("Em que número eu pensei?"))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Você acertou")
else:
    print("Você ERROU!!!")
    print("Eu pensei no número {}, e não no {}!".format(computador, jogador))
    print("Tente mais uma vez!")
