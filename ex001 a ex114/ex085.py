princ = [[], []]
n = 0
for i in range(1, 8):
    n = int(input(f"Digite o {i}° valor: "))
    if n % 2 == 0:
       princ[0].append(n)
    elif n % 2 == 1:
        princ[1].append(n)
print("-="*15)
print(f"Os pares são {sorted(princ[0])}")
print(f"Os impares são {sorted(princ[1])}")

