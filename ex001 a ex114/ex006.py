import math

n1 = float(input("Digite um número: "))
d = n1 * 2
t = n1 * 3
r = math.sqrt(n1) #ou pode ser assim, de uma forma mais simples: n ** (1/2)
print("O dobro de {} é {}".format(n1, d))
print("O triplo de {} é {}".format(n1, t))
print("A raiz quadrada de {} é {:.3}".format(n1, r))