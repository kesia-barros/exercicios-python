cont = 0
n = (int(input("Digite um numero: ")),
     int(input("Digite outro numero: ")),
     int(input("Digite mais um numero: ")),
     int(input("Digite o ultimo numero: ")))
print(f"Você digitou os valores: {n}")
print(f"O valor 9 aparece {n.count(9)} vezes.")
if 3 in n:
     print(f"O valor 3 aparece na posição {n.index(3)+1}")
else:
     print("O valor 3 não foi digitado em nenhuma posição.")
print(f"Os numeros pares digitados foram: ", end="")
for num in n:
     if num % 2 == 0:
          print(num, end=" ")
