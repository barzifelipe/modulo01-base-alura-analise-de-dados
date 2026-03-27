contador = 0

while contador < 3:
    nota = float(input("Insira uma nota válida (de 0 a 5 ): "))

    if nota <= 5 and nota >= 0:
        print("Nota computada! ")
        contador += 1
        
    else:
        print("Nota inválida. Tente novamente.")
       
