s = 0
cont = 0
for i in range(1, 500, 2):
    if i%3 == 0:
        cont = cont + 1
        s = s + i
print("A soma de todos os {} valores solicitadoas é {}".format(cont, s))