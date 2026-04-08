gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

total_acertos = 0

for i in range (10):
    resposta = input(f"Digite sua resposta na questão {i+1}: ").strip().upper()

    if resposta == gabarito[i]:
        total_acertos += 1


print(total_acertos)
