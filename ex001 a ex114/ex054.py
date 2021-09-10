from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input("Em que ano a {}° pessoa nasceu? ".format(i)))
    idade = atual - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print("{} pessoas são maior".format(totmaior))
print("{} pessoas são menor".format(totmenor))