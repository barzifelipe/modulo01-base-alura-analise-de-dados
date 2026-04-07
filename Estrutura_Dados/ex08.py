total_doce = 0
total_amargo = 0

lista = []
for i in range(10):
    id = int(input("Digite um ID: "))
    lista.append(id)

for codigo in lista:
    if id % 2 == 0:
        total_doce += 1
    
    else: 
        total_amargo += 1

print(f"Total de produtos doces: {total_doce}")
print(f"Total de produtos amargos: {total_amargo}")

