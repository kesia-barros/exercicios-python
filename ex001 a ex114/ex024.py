cid = input("Qual o nome da sua cidade?").strip()
print(cid[:5].upper() == "SANTO")  # o programa deixa o nome da cidade todo em maiusculo e procura a palavra santo
# isso serve para não ter erro na hora do usuaria escrever, ele pode usar maiusculas ou minusculas pra escrever, ou os dois juntos que mesmo assim o programa acha.



'''nome = "Santo" in cid
if nome == True:
    print("Sua cidade contém Santo no nome.")
else:
    print("Sua cidade não contém Santo no nome.")'''