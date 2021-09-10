num = []
maior = 0
menor = 0
for i in range(0, 5):
    num.append(int(input(f"Digite um numero para a posição {i}: ")))
    if i == 0:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
print("*-" * 18)
print(f"Você digitou os numeros {num}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(num):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(num):
    if v == menor:
        print(f"{i}...", end="")
print()




