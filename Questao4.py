pa = 80000
pb = 200000
ano = 0

while pb > pa:
    pa += pa * 0.03
    pb += pb * 0.015
    ano += 1


print("Quantidade de anos necessários para igualara população dos paises é: ", ano)
