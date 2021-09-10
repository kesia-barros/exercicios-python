lista_num = []
while True:
    n = int(input("Digite um numero: "))
    lista_num.append(n)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == "N":
        break
if 5 in lista_num:
    print("O numero 5 esta na lista!")
else:
    print("O numero 5 não esta na lista...")
print(f"Foram digitados {len(lista_num)} numeros ao todo.")
print(f"Lista ordenada de forma decrescente {sorted(lista_num, reverse=True)}")