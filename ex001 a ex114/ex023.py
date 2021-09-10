num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Milhar", m)
print("Centenas", c)
print("Dezenas", d)
print("Unidade", u)




'''num = (input("Digite um número de 0 a 9999: "))
print("Milhar",num[0])
print("Centenas",num[1])
print("Dezenas",num[2])
print("Unidade",num[3])'''