from time import sleep


def ajuda(com):
    help(com)


def titulo(msg):
    print("~-*" * len(msg))
    print(msg.center(len(msg)*3))
    print("~-*" * len(msg))


def escreva(msg):
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))

n = ' '
while n != "fim":
    titulo("SISTEMA DE AJUDA PYHELP")
    n = input("Função ou Biblioteca >").lower()
    if n == "fim":
        break
    escreva(f"Acessando o Manual do comando '{n}'...")
    sleep(5)
    ajuda(n)