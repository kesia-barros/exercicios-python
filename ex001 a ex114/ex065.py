resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    if quant == 1:  # quant indica a posição,neste caso se trata do primeiro número digitado.
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Quer continuar? [S/N]")).upper().strip()
media = soma / quant
print("Você digitou {} números e a média foi: {}".format(quant, media))
print("O maior valor foi {} e menor foi {}.".format(maior, menor))