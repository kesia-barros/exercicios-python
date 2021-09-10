s = cont = 0
while True:
    n = int(input("Digite um número [0 para parar]: "))
    if n == 0:
        break
    s += n
    cont += 1
print(f"Foram digitados {cont} números e a soma entre eles é {s}.")