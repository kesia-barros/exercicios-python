l1 = [[], [], []]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        l1[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{l1[l][c]:^5}", end="")
    print()
