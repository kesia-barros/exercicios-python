from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ", flush=True)
            sleep(1)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}",end=" ", flush=True)
            sleep(1)
            cont -= passo
        print("FIM!")

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)