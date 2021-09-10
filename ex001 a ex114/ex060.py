'''from math import factorial
n = int(input("Digite um número: "))
f = factorial(n)
print("Calculando o fatorial de {}! = {}".format(n, f))

# outra forma de fazer:

n = int(input("Digite um número: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{} ".format(c), end="")
    print("X " if c > 1 else " = ", end="")
    f = f * c
    c = c - 1
print("{}".format(f))'''

# outra forma de fazer:

n = int(input("Digite um número: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
for i in range(n, 1, -1):
    print("{} ".format(c), end="")
    print("X " if c > 1 else " = ", end="")
    f = f * c
    c = c - 1
print("{}".format(f))