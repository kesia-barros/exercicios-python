frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras) # tirando os espaços entre as palavras, juntando para separar letras inves das palavras inteiras.
inverso = ""
for i in range(len(junto)-1, -1, -1): # colocando -1 para o python pegar a ultima letra indo de tras pra frente.
    inverso = inverso + junto[i]
if inverso == junto:
    print(frase, "/", inverso)
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
print("Você digitou a frase: {} ".format(frase))

# outra forma de fazer : sem o for

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras) # tirando os espaços entre as palavras, juntando para separar letras inves das palavras inteiras.
inverso = junto[::-1] # dentro do colchete: começa no inicioda frase, termina no fim da frase, de tras pra frente.
if inverso == junto:
    print(frase, "/", inverso)
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
print("Você digitou a frase: {} ".format(frase))