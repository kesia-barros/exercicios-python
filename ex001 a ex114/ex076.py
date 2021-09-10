lista = ('Lapis', 1.75,'Borracha', 2.00, "Caderno", 15.00,
         "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99,
         "Mochila", 120.32, "Canetas", 22.30, "livro", 34.90)
print("-="*20)
print("          LISTAGEM DE PREÇOS")
print("-="*20)
for pos in range(0, len(lista)):  #  vai de 0 ate o tamanho da lista por isso se usa o len()
    if pos % 2 == 0:  # se a posição for par
        print(f"{lista[pos]:.<30}", end="")
    else:
        print(f"R${lista[pos]:>7.2f}")
print("-="*20)

#outra forma de fazer:

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)
for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", end="")
    print(f"R$ {produtos[c+1]:>7.2f}")
print("="*50)