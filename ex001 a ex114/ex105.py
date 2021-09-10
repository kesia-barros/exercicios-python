def notas(*n, situacao=False):
    r = {}
    r["Total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if situacao:
        if r["media"] >= 7:
            r["situação"] = "BOA"
        elif r["media"] >= 5:
            r["situação"] = "RAZOAVEL"
        else:
            r["situação"] = "RUIM"
    return r


resp = notas(5.5, 2.5, 8.5, situacao=True)
print(resp)