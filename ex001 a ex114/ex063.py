print("-"*30)
print("Sequencia de Fibonacci")
print("-"*30)
n = int(input("Quantos termos você quer mostrar?"))
t1 = 0
t2 = 1
print("~"*30)
print("{} -> {}".format(t1, t2), end="")
cont = 3 # o cont vai iniciar com valor 3, pq ja mostrei 3 termos
while cont <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2 # para fazer um loop para somar os termos, basta colocar t1 no lugar do t2 ->
    t2 = t3  # e o t2 no lugar do t3, e depois começa o loop
    cont = cont + 1
print(" -> FIM")