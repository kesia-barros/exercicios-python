times = ("Bragantino", "Athletico-PR", "Palmeiras", "Fortaleza",
         "Bahia", "Santós", "Atlético-GO", "Atlético-MG",
         "Fluminense", "Flamengo", "Corinthians", "Ceará SC",
         "Internacional", "Juventude", "Sport Recife", "Cuiabá",
         "São Paulo", "Chapecoence", "América-MG", "Grêmio")
print("-="*30)
print(f"Lista de time {times}")
print("-="*30)
print(f"Os 5 primeiros colocados são: {times[0:5]}.")
print("-="*30)
print(f"Ultimos 4 colocados são: {times[-4:]}.")
print("-="*30)
print(f"Lista dos time em ordem alfabetica: {sorted(times)}.")
print("-="*30)
print(f"A chapecoence esta na {times.index('Chapecoence')+1}° posição.")