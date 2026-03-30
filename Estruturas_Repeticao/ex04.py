soma = 0
contador = 0

while True:
    temp = float(input("Digite uma temperatura em Celsius (-273 para parar): "))

    if temp == -273:
        break

    soma += temp
    contador += 1

if contador > 0:
    media = soma/contador
    print(f"A média das temperaturas é: {media}")
    
else: 
    print("Nenhuma temperatura válida foi informada")
