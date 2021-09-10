from random import randint

computador = randint(0, 10)
print("Escolha um numero de 0 entre 10 ")
acertou = False
cont = 0
while not acertou:
    jogador = int(input("Em que número eu pensei?"))
    cont = cont + 1
    if jogador == computador:
        acertou = True
        print("Você acertou")
        print("Escolhi o número {}!".format(computador))
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos...")
print("Você fez em {} tentativas!".format(cont))
