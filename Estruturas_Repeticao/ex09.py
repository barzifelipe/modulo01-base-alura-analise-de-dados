candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

for i in range (20):
    voto = int(input("Digite seu voto: "))

    if voto == 1:
        candidato1 += 1

    elif voto == 2:
        candidato2 += 1
    
    elif voto == 3:
        candidato3 += 1

    elif voto == 4:
        candidato4 += 1
    
    elif voto == 5:
        nulo += 1
    
    elif voto == 6:
        branco += 1

porcentagemNulo = (nulo/20)*100
porcentagemBranco = (branco/20)*100

print("\nResultados:")
print(f"Candidato 1: {candidato1}")
print(f"Candidato 2: {candidato2}")
print(f"Candidato 3: {candidato3}")
print(f"Candidato 4: {candidato4}")
print(f"Nulos: {nulo}")
print(f"Branco: {branco}")
print(f"Porcentagem de votos nulos: {porcentagemNulo}%")
print(f"Porcentagem de votos brancos: {porcentagemBranco}%")