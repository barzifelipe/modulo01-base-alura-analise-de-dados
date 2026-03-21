def main():

    lado1 = float(input("Digite a medida do lado 1: "))
    lado2 = float(input("Digite a medida do lado 2: "))
    lado3 = float(input("Digite a medida do lado 3: "))

    verificacao = verificar(lado1, lado2, lado3)

    classificar(verificacao, lado1, lado2, lado3)

def verificar(lado1, lado2, lado3):
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

def classificar(verificacao, lado1, lado2, lado3):

    if verificacao == True:
        if lado1 == lado2 and lado1 == lado3:
            print("Equilatero")   
        
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Isósceles")

        else:
            print("Escaleno")    

    else:
        print("Não é um triângulo")

main()