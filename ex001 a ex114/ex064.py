n = val = s = 0
while n != 999:
    n = int(input("Digite um número [999 para parar]:  "))
    if n != 999:
        val += 1
        s = s + n
print("O número de valores digitados foi {}".format(val))
print("A soma entre esses valores é: {}".format(s))