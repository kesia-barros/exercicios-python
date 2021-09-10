r1 = float(input("Digite o comprimento da 1° reta: "))
r2 = float(input("Digite o comprimento da 2° reta: "))
r3 = float(input("Digite o comprimento da 3° reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triangulo!")
else:
    print("Não pode formar um triangulo!")
