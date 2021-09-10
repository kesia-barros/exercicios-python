def aumentar(num=0, porcent=0):
    aumento = num + (porcent/100*num)
    return aumento


def diminuir(num=0, porcent=0):
    diminuto = num - (porcent/100*num)
    return diminuto


def dobro(num=0):
    dob = num*2
    return dob


def metade(num=0):
    met = num/2
    return met


def moedas(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')