num = int(input("Digite um número: "))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=" ")
        tot = tot + 1
    else:
        print("\033[31m",end=" ")
    print("{}".format(i), end=" ")
print("\n\033[mO número {} foi divisivel {} vezes".format(num, tot))
if tot == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele NÃO é primo!")