def aumentar(num=0, taxa=0, formato=False):
    aumento = num + (taxa/100*num)
    return aumento if formato is False else moedas(aumento)


def diminuir(num=0, taxa=0, formato=False):
    diminuto = num - (taxa/100*num)
    return diminuto if formato is False else moedas(diminuto)


def dobro(num=0, formato=False):
    dob = num*2
    return dob if formato is False else moedas(dob)


def metade(num=0, formato=False):
    met = num/2
    return met if formato is False else moedas(met)


def moedas(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, taxaaumen=10, taxareduc=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço Analisado: \t{moedas(num)}")
    print(f"Dobro do valor: \t{dobro(num, True)}")
    print(f"Metade do valor: \t{metade(num, True)}")
    print(f"{taxaaumen}% de aumento: \t{aumentar(num, taxaaumen, True)}")
    print(f"{taxareduc}% de redução: \t{diminuir(num, taxareduc, True)}")
    print("-" * 30)