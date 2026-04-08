salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = []

contador_minimo = 0

for salario in salarios:
    abono = salario/10

    if abono < 200:
        abono = 200
        contador_minimo += 1

    abonos.append(abono)

dicionario = dict(zip(salarios, abonos))

total_gastos = sum(dicionario.values())
maior_abono = max(dicionario.values())

print("Dicionário:", dicionario)
print("Total de gastos com abono:", total_gastos)
print("Quantidade de colaboradores com abono mínimo:", contador_minimo)
print("Maior valor de abono:", maior_abono)