import requests
try:
    pudim = requests.get("http://pudim.com.br/")
except:
    print("No momento o site não esta no ar!")
else:
    print("Acessou ao site com sucesso!!!")