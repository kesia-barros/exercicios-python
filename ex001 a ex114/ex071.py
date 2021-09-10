valor = int(input("Informe o valor que deseja sacar: R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:  # se o valor for maior que a cedula
        total -= ced  # vair tirar o falor da cedula do valor ex: valor 200 reais, tira 50, tira mais 50... até 0, que 4 notas de 50
        totced += 1
    else:
        if totced > 0:  # só escreve se o total de cedulas for maior que 0
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:  # se eu nao conseguir mais tirar 50 eu passa para a proxima nota
            ced = 20  # que é a nota de 20 reais, e assim sucessivamente
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break