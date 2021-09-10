numeros = []
while True:
    n = int(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
        print("Adicionado com sucesso!")
    else:
        print("Valor duplicado, não vou adicionar...")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if continuar == "N":
        break
print(sorted(numeros))