preco1 = float(input("Digite a media de preço no ano 1: "))
preco2 = float(input("Digite a media de preço no ano 2: "))
preco3 = float(input("Digite a media de preço no ano 3: "))

if preco1 > preco2 and preco1 > preco3:
    print("O preço no ano 1 é o maior")
elif preco2 > preco1 and preco2 > preco3:
    print("O preço no ano 2 é o maior")
else:
   print("O preço no ano 3 é o maior")