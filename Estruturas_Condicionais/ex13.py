def main():
    vendas2022 = float(input("Digite o valor de vendas de 2022: "))
    vendas2023 = float(input("Digite o valor de vendas de 2023: "))

    variacao = calcularVariacao(vendas2022,vendas2023)

    print(f"Variação percentual: {variacao:.2f}%")
    
    verificarVariacao(variacao)

def calcularVariacao(vendas2022, vendas2023):
    return (vendas2023-vendas2022/vendas2022)*100

def verificarVariacao(variacao):
    if variacao > 20:
        print("Bonificação para o time de vendas")

    elif variacao > 2:
        print("Pequena bonificação para time de vendas")

    elif variacao >= -10:
        print("Planejamento de políticas de incentivo às vendas")

    else:
        print("Corte de gastos")


main()