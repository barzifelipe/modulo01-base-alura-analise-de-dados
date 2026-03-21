def main():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    operacao = input("Qual a operação que você deseja realizar? ").lower()
    
    resultado = calculadora(operacao, num1, num2)
    
    if resultado is not None:
     print(f"Resultado: {resultado}")
     classificar(resultado)
    
    else:
        print("Não foi possível calcular")


def calculadora(operacao, num1, num2):
    
    if operacao == "soma":
        return num1+num2
    
    elif operacao == "subtração":
         return num1-num2
    
    elif operacao == "multiplicação":
         return num1*num2
    
    elif operacao == "divisão":
         if num2 == 0:
             print("Erro: divisão por zero")
             return None
         
         return num1/num2
       
    else:
        print("Opção inválida")  
        return None     


def classificar(resultado):
    
    if resultado.is_integer():
        if int(resultado) % 2 == 0:
            print("É par")
        else:
            print("É ímpar")
    else:
        print("Não é inteiro, então não pode ser par ou ímpar")
    
    if resultado > 0:
        print("É positivo")
    
    elif resultado < 0:
        print("É negativo")

    else: 
        print("É zero")

    if resultado.is_integer():
        print("É inteiro")
    else:
        print("É decimal")


main()