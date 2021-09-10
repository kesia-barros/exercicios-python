def escreva(msg):
    print("~-*" * len(msg))
    print(msg.center(len(msg)*3))  # *3 pode variar de acordo com o tanto de simbolos que coloco nas linhas neste caso "~-*", foram 3 simbolos
    print("~-*" * len(msg))


msg = str(input("Digite uma mensagem: "))
escreva(msg)