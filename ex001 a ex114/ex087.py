l1 = [[], [], []]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        l1[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{l1[l][c]:^5}", end="")
        if l1[l][c] % 2 == 0:
            spar += l1[l][c]
    print()
print("-="*30)
print(f"A soma dos valores pares e {spar}.")
for l in range(0, 3):
    scol += l1[l][2]
print(f"A soama dos valores da terceira coluna e {scol}.")
for c in range(0, 3):
   if c == 0:
       mai = l1[1][c]
   elif l1[1][c] > mai:
       mai = l1[1][c]
print(f"O maior valor da segunda linha e {mai}.")