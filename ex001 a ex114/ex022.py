nome = str(input("Escreva seu nome completo: ")).strip()  # .strip() para eliminar os espaços antes e depois caso o usuario de espaços desnecessarios.
print("Seu nome em minusculas: ",nome.lower())
print("Seu nome em maiusculas: ",nome.upper())
print("Seu nome completo tem {} letras!".format(len(nome.replace(" ", ""))))
print("Seu primeiro nome tem {} letras!".format(nome.find(" ")))

# outra forma de se fazer:
nome = str(input("Escreva seu nome completo: ")).strip()  # .strip() para eliminar os espaços antes e depois caso o usuario de espaços desnecessarios.
print("Seu nome em minusculas: ",nome.lower())
print("Seu nome em maiusculas: ",nome.upper())
print("Seu nome completo tem {} letras!".format(len(nome) - nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome tem {} letras!".format(len(separa[0])))

