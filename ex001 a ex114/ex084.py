nome_peso = []
temp = []
maior = menor = cont = 0
while True:
    cont += 1
    temp.append(str(input("Digite seu nome: ")))
    temp.append(float(input("Digite seu peso atual: ")))
    if len(nome_peso) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    nome_peso.append(temp[:])
    temp.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == "N":
        break
print(nome_peso)
print(f"{cont} pessoas se cadastraram")
print(f"O maior peso e {maior}Kg ", end=" ")
for p in nome_peso:
    if p[1] == maior:
        print(f"{p[0]}")
print(f"O menor peso e {menor}Kg ", end=" ")
for p in nome_peso:
    if p[1] == menor:
        print(f"{p[0]}")