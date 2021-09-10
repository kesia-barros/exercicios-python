def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return (f"Com idade {idade}: Não Vota!")
    elif 16 <= idade < 18:
       return (f"Com idade {idade}:  Voto opcional!")
    elif idade >= 18:
        return (f"Com idade {idade}: Voto obrigatorio!")

print("*-"*15)
ano_nasc = int(input("Qual o ano do seu nascimento? "))
print(voto(ano_nasc))


