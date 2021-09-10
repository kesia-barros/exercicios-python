from random import randint

jogador = s = resultado = vitorias = 0
while True:
    jogador = int(input("Digite um número até 10: "))
    escolha = str(input("PAR ou IMPAR")).strip().lower()
    print("-=" * 25)
    computador = randint(0, 10)
    s = jogador + computador
    if s % 2 == 0:
        resultado = "par"
    if s % 2 == 1:
        resultado = "impar"
    print(f"Você jogou {jogador} e o computador {computador}. Total deu {s} e {s} é {resultado}")
    if escolha == resultado:
        vitorias += 1
        print("-=" * 25)
        print("Você ganhou!")
    else:
        print("-=" * 25)
        print(f"Perdeu!!! Você venceu {vitorias} vezes.")
        break

