valor = float(input("Qual o valor do produto?"))
print(" ")
print(''' -=-=-=-=-=-= FORMAS DE PAGAMENTO =-=-=-=-=-=-
1 - À vista no dinheiro/cheque: desconto 10%
2 - À vista no cartão: desconto 5%
3 - Em até 2x no cartão: preço valor_normal
4 - 3 x ou mais no cartão: juros 20%''')
print("-"*45)
print(" ")
condicao_pagamento = int(input("Qual a condição de pagamento?"))
if condicao_pagamento == 1:
    total = valor - (valor * 0.10)
    print("O valor total deu {} reais.".format(total))
elif condicao_pagamento == 2:
    total = valor - (valor * 0.05)
    print("O valor total deu {} reais.".format(total))
elif condicao_pagamento == 3:
    total = valor
    parcelas = total / 2
    print("Serão 2 prestações no valor de {} reais.".format(parcelas))
    print("O valor total deu {} reais.".format(total))
elif condicao_pagamento == 4:
    total = valor + (valor * 0.20)
    totparc = int(input("Quantas parcelas? "))
    parcelas = total / totparc
    print("Sua compra será parcelada em {}X de R${:.2f} reais, com juros de 20%".format(totparc, parcelas ))
    print("O valor total no final dará, R${} reais.".format(total))
else:
    print("Por favor escolha uma das opções disponiveis")