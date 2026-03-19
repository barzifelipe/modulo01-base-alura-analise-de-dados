def main():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    operacao = input("Qual a operação que você deseja realizar? ").lower()
    calculadora(operacao, num1, num2)


def calculadora(operacao, num1, num2):
    if operacao == "soma":
        print(num1 + num2)
    elif operacao == "subtração":
        print(num1-num2)
    elif operacao == "multiplicação":
        print(num1*num2)
    elif operacao == "divisão":
        print(num1/num2)
    else:
        print("Opção inválida")       


main()