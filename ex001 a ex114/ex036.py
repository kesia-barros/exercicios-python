print("-="*20)
print("         EMPRESTIMO BANCÁRIO")
print("-="*20)
valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salario? "))
anos_pagar = float(input("Em quantos anos voê quer pagar?"))
prestacao = valor_casa / (anos_pagar * 12)
porcentagem_sal = salario * 0.30
if prestacao > porcentagem_sal:
    print("\033[31mEmpréstimo NEGADO!\033[m")
else:
    print("\033[32mEmprestimo APROVADO!!!\033[m")
    print("O valor das prestações seram R${:.2f} reais por mês, durante {} anos!".format(prestacao, anos_pagar))