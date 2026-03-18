entrada = input("Digite uma letra: ")
letra = entrada[0].lower()

if letra in 'aeiou':
    print("A letra é uma vogal")
else:
    print("A letra é uma consoante")