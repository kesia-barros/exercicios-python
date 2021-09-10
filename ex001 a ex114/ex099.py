def maior(* num):
    mai = cont = 0
    for i in num:
        print(f"{i}", end=" ", flush=True)
        if cont == 0:
            mai = i
        else:
           if i > mai:
                mai = i
        cont += 1
    print(f"\nForam informados {cont} numeros.")
    print(f"O maior numero e {mai}")
    print("-=" * 20)




maior(2, 3, 6, 8)
maior(3, 1, 9, 0)
maior(1, 10)
