from random import sample

num = tuple(sample(range(10), 5))
print(f"Eu sorteei os valores: ", end="")
for tupla in num:
       print(f"{tupla} ", end="")
print(f"\nO menor entre eles e: {min(num)}")
print(f"O maior entre eles e: {max(num)}")

#outra forma mais simples:
from random import sample
a = tuple(sample(range(10), 5))
print(f'Os números sorteados foram: {a}\nO maior valor é {max(a)} e o menor é {min(a)}.')