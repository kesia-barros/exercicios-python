from ex108 import moeda

n = float(input("Digite um valor: R$ "))
print(f"A metade de {moeda.moedas(n)} e {moeda.moedas(moeda.metade(n))}")
print(f"O dobro de {moeda.moedas(n)} e {moeda.moedas(moeda.dobro(n))}")
print(f"O aumento de 10%, temos {moeda.moedas(moeda.aumentar(n, 10))}")
print(f"A redução de 13%, temos {moeda.moedas(moeda.diminuir(n, 13))}")