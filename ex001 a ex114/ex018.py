import math

an = float(input("Digite um angulo: "))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.tan(an))
print("O seno de {} é,{:.2f}".format(an, seno))
print("O cosseno de {} é,{:.2f}".format(an, cos))
print("A tangente de {} é,{:.2f}".format(an, tan))