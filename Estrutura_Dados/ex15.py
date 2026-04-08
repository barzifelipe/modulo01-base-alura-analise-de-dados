dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

medias = {}

contador = 0

for setor, idades in dados.items():
    media = sum(idades)/len(idades)
    medias[setor] = media

media_geral = sum(medias.values())/len(medias)

for idades in dados.values():
    for idade in idades:
        if media_geral > idade:
            contador += 1

print("Médias por setor:")
for setor, media in medias.items():
    print(f"{setor}: {media:.2f}")

print(f"Média geral: {media_geral}")

print(f"Estão acima da média {contador} pessoas")