lista_num = []
lista_pares = []
lista_impares = []
while True:
    n = int(input("Digite um numero: "))
    lista_num.append(n)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continar? [S/N]: ")).strip().upper()
    if resp == "N":
            break
for i, v in enumerate(lista_num):
    if v % 2 == 0:
        lista_pares.append(v)
    if v % 2 == 1:
        lista_impares.append(v)
print(f"Você digitou os valores: {lista_num}")
print(f"Os numeros pares digitados foram: {lista_pares}")
print(f"Os numeros impares digitados foram: {lista_impares}")
