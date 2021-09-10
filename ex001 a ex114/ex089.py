dados = []
lista = []
media = 0
while True:
   nome = str(input("Digite seu nome: "))
   n1 = float(input("Digite sua 1° nota: "))
   n2 = float(input("Digite sua 2° nota: "))
   media = (n1 + n2) / 2
   dados.append(nome) # [0]
   dados.append(n1)  # [1]
   dados.append(n2)  # [2]
   dados.append(media)  # [3]
   lista.append(dados[:])
   dados.clear()
   resp = ' '
   while resp not in "SN":
       resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
   if resp == "N":
    break
print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("-="*30)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[3]:>8.1f}")
while True:
    print("-=" * 30)
    opc = int(input("Mostra notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f"Notas de {lista[opc][0]} são {lista[opc][1]} e {lista[opc][2]}")
print("FINALIZANDO...")