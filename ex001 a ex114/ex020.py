import random

a1 = str(input("Digite o nome do 1° aluno: "))
a2 = str(input("Digite o nome do 2° aluno: "))
a3 = str(input("Digite o nome do 3° aluno: "))
a4 = str(input("Digite o nome do 4° aluno: "))
a5 = str(input("Digite o nome do 5° aluno: "))
aluno = [a1, a2, a3, a4, a5]
random.shuffle(aluno)
print("Ordem de alunos que irão apresentar é: ", aluno)