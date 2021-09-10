from random import randint


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for i in range(0, 5):
        n = randint(1, 20)
        lista.append(n)
        print(f"{n}", end=" ")




def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"\nSomando os valores pares de {lista}, temos {soma}")


numeros = []
sorteia(numeros)
soma_par(numeros)




