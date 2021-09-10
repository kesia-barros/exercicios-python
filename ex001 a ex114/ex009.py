n1=int(input("Digite um número entre 1 e 10: "))
n2=0
n3=0
for i in range(10):
    n2 = n2 + 1
    n3 = n1 * n2
    print("{} X {:2} = {}".format(n1, n2, n3))
