d = int(input("quantos dias foi alugado?"))
km = float(input("Quantos km rodados?"))
p = (d*60) + (km*0.15)
print("O total a pagar é de R${:.2f}".format(p))