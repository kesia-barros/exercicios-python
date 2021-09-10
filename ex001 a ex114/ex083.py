exp = str(input("Digite uma expressão: "))
pilha = []
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:  # se o tamanho da lista for maior que zero
            pilha.pop() # eliminar o ultimo elelmento da lista
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão esta valida!")
else:
    print("Sua expressão esta errada!")

# outra forma:

exp = str(input("Digite uma expressão:"))
pilha = 0
for simb in exp:
    if simb == "(":
        pilha += 1
    if simb == ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")