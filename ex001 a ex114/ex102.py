def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" X ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


n = int(input("Digite um numero: "))
mostrar = str(input("Você quer mostrar o calculo [S/N]: ")).strip().upper()[0]
if mostrar == "S":
    mostrar = fatorial(n,show= True)
    print(mostrar)
else:
    print(f"O fatorial de {n} e igual a {fatorial(n)}")