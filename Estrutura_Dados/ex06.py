data = input("Digite uma data (dd/mm/aaaa): ")
lista = data.split('/')

dia = int(lista[0])
mes = int(lista[1])

if dia > 31:
    print("Data inválida")

elif mes > 12:
    print("Data inválida")

else:
    print(lista)