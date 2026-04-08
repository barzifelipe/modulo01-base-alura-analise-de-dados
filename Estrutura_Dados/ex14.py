dados = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

medias = {}

for area, valores in dados.items():
    media = sum(valores)/len(valores)
    medias[area] = media

maior_area = max(medias, key=medias.get)

print("Médias por área:")
for area, media in medias.items():
    print(f"{area}: {media:.2f}")

print(f"\nÁrea com maior diversidade biológica: {maior_area}")