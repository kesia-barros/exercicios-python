lista_num = ('zero' , 'um', 'dois', 'três', 'quatro',
             'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze', 'quatorze',
             'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'desenove', 'vinte',)
while True:
    n = int(input("Digite um número de 0 a 20: "))
    if 0 < n > 20:
        print("Tente novamente.", end="")
    else:
        print(f"Você digitou o número {lista_num[n]}")
        resp = " "
        while resp not in "sn":
            resp = str(input("Quer continuar? [S/N]")).strip().lower()
            if resp == "n":
                break
