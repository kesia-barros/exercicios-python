n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
r = 0
while r != 5:
    print('''O que você deseja fazer?
    MENU:
    [1] Somar.
    [2] Multiplicar.
    [3] Maior
    [4] Novos números.
    [5] Sair do programa.''')
    r = int(input("Opção: "))
    if r == 1:
        s = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, s))
        print("-="*15)
    elif r == 2:
        m = n1 * n2
        print("O resultado de {} X {} é {}".format(n1, n2, m))
        print("-=" * 15)
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior é {}!".format(n1, n2, maior))
        print("-=" * 15)
    elif r == 4:
        print("Informe os números novamente: ")
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))
    elif r == 5:
        print("FINALIZANDO...")
    else:
        print("Opção invalida! Tente novamente!")