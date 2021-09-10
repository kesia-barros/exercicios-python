from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'exercicio115.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    opcao = menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoas.', 'Sair do Sistema.'])

    if opcao == 1:
        leiaarquivo(arq)

    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Digite o nome: "))
        idade = leiaint("Digite a idade: ")
        cadastrar(arq, nome, idade)


    elif opcao == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
    sleep(2)
