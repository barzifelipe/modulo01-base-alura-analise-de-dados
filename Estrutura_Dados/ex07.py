lista = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

listaCrescimento = []

for i in range (1, len(lista)):
    percentual = round(100*(lista[i]-lista[i-1])/lista[i-1])
    listaCrescimento.append(percentual)

print(listaCrescimento)