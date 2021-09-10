V = float(input("Qual a distancia da viagem?"))
if V <= 200:
    custo = V * 0.50
else:
    custo = V * 0.45
print("O custo será de: R${} reais.".format(custo))
print("Boa viagem!")