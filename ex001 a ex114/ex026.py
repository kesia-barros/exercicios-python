frase = input("Digite uma frase:").lower().strip()
print("A letra 'a' aparece {} vezes.".format(frase.count("a")))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find("a")+1))
print("A letra 'a' aparece por ultimo na posição {}".format(frase.rfind("a")+1))  # o +1 serve pra adequar a posição do python, pois o python inicia do 0, mas eu quero que inicie do 1