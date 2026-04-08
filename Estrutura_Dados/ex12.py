votos = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210,
    "Design 5": 1811
}

print(max(votos, key=votos.get))
total_votos = sum(votos.values())

porcentagem_votos = (max(votos.values())/total_votos)*100
print(f"{porcentagem_votos:.2f}%")