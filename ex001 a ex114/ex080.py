lista = []
for i in range(0, 5):
    n = int(input("Digite um numero: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print(f"Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:  # se n for menor ou = a lista na posição pos
                lista.insert(pos, n)  # na posição pos insira n
                print(f"Adicionado a posição {pos} da lista.")
                break
            pos += 1
print(f"Os valores digitados foram: {lista}")

