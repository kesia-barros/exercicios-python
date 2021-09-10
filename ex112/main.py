from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dados

n = dados.leiadinheiro("Digite um valor: R$ ")
moeda.resumo(n, 80, 35)