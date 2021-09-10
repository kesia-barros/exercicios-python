while True:
    print("-=" * 20)
    n = int(input("Digite um número para ver sua tabuada: "))
    if n < 0:
        print("-="*20)
        print("Programa tabuada encerrado!".upper())
        break
    for i in range(0, 11):
        print(f"{n} X {i} = {n*i}")