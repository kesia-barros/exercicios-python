primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo_termo + razao, razao):
    print("{} ".format(i), end="-> ")
print("ACABOU")