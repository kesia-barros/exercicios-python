s = 0
cont = 0
for i in range(1, 7):
    par = int(input("Digite o {} número: ".format(i)))
    if par % 2 == 0:
        s = s + par
        cont = cont + 1 # para contar quantos numeros pares a pessoa digitou
print("Você informou {} valores pares e soma deles é: {} ".format(cont, s))