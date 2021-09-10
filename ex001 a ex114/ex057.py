sexo = str(input("Qual o seu sexo?")).strip().upper()[0]   #esta tirando os espaços, mandando todads as letras para a maiuscula.
# [0] fazendo pegar só a primeira letra, o usuario pode escrever uma frase ou uma palavra mas vai pegar só a primeira letra.
while sexo not in "MF":
    print("Valor incorreto! Tente novamente!")
    sexo = str(input("Qual o seu sexo?")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))