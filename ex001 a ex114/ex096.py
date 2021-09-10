def area(a, b):
    print(f"O comprimento e {a} e a largura e {b}")
    c = a * b
    print(f"A area deste terreno e de {c}m²")

#programa principal
a = float(input("COMPRIMENTO (m): "))
b = float(input("LARGURA (m): "))
print("*-" * 20)
area(a, b)
