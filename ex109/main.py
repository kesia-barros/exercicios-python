from ex109 import moeda

n = float(input("Digite um valor: R$ "))
print(f"A metade de {moeda.moedas(n)} e {moeda.metade(n, True)}")
print(f"O dobro de {moeda.moedas(n)} e {moeda.dobro(n, True)}")
print(f"O aumento de 10%, temos {moeda.aumentar(n, 10, True)}")
print(f"A redução de 13%, temos {moeda.diminuir(n, 13, True)}")