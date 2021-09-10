def aumentar(num=0, porcent=0, formato=False):
    aumento = num + (porcent/100*num)
    return aumento if formato is False else moedas(aumento)


def diminuir(num=0, porcent=0, formato=False):
    diminuto = num - (porcent/100*num)
    return diminuto if formato is False else moedas(diminuto)


def dobro(num=0, formato=False):
    dob = num*2
    return dob if formato is False else moedas(dob)


def metade(num=0, formato=False):
    met = num/2
    return met if formato is False else moedas(met)


def moedas(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')