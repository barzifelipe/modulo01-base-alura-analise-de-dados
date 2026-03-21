def main():
    qtdLitro = float(input("Quantos litros foram vendidos? "))
    tipoCombustivel = input("Qual foi o tipo de combustível? Etanol (E) ou Diesel (D)").upper()
    
    resultado = calcular(qtdLitro, tipoCombustivel)
    
    if resultado is not None:
        print(f"O valor final a ser pago é: R$ {resultado:.2f}")
    else:
        print("Não foi possível calcular.")

def calcular(qtdLitro, tipoCombustivel):
    if tipoCombustivel == "E":
        valorBruto = qtdLitro*1.70

        if qtdLitro <= 15:
            desconto = valorBruto * 0.02
        
        else:
            desconto = valorBruto * 0.04
            
        return valorBruto - desconto 
    
    elif tipoCombustivel == "D":
        valorBruto = qtdLitro*2

        if qtdLitro <= 15:
            desconto = valorBruto * 0.03
        
        else:
            desconto = valorBruto * 0.05
            
        return valorBruto - desconto 
    
    else:
        return None

main()