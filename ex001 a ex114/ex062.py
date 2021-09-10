print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10 # para começar ja mostrando 10 termos
while mais != 0:
    total = total + mais # total vai começar com 10
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print("Progressão finalida com {} termos mostrados.".format(total))