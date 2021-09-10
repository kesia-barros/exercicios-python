from ex107 import moeda

n = float(input("Digite um valor: R$ "))
print(f"A metade de {n} e {moeda.metade(n)}")
print(f"O dobro de {n} e {moeda.dobro(n)}")
print(f"O aumento de 10%, temos {moeda.aumentar(n, 10)}")
print(f"A redução de 13%, temos {moeda.diminuir(n, 13)}")