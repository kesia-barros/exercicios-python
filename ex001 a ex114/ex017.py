import math

co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("O comprimento da hipotenusa é, {:.2f}".format(hi))

# Outra forma de fazer é:
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("O comprimento da hipotenusa é, {:.2f}".format(hi))