nome = input("Digite seu nome completo: ").strip()
s = "SILVA" in nome.upper()  # ou s = "silva" in nome.lower(), tambem funciona.
if s == True:
    print("Seu nome contém Silva.")
else:
    print("Seu nome não contem Silva.")