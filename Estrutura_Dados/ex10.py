lista = []
somaTemp = 0

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

for i in range (12):
    mediaMensal = float(input(f"Digite a temperatura do mês {i}: "))
    lista.append(mediaMensal)
    somaTemp += mediaMensal

mediaAnual = somaTemp/12

print(f"\nMédia anual: {mediaAnual:.2f}\n")

for i in range(12):
    if lista[i] > mediaAnual:
        print(f"{meses[i]}: {lista[i]}")

