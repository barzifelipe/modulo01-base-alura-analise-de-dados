faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

idade = int(input("Digite uma idade: " ))

while idade >= 0:
    if idade <= 25:
        faixa1 += 1
    
    elif idade <= 50:
        faixa2 += 1

    elif idade <= 75:
        faixa3 += 1
    
    elif idade <= 100:
        faixa4 += 1

    idade = int(input("Digite uma idade: " ))

print("\nDistribuição de idades:")
print(f"[0-25]: {faixa1}")
print(f"[26-50]: {faixa2}")
print(f"[51-75]: {faixa3}")
print(f"[76-100]: {faixa4}")