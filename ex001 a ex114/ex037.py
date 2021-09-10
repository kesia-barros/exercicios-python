num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO.
[ 2 ] converter para OCTAL.
[ 3 ] coverter para HEXADECIMAL.''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para BINARIO é a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é a {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida")