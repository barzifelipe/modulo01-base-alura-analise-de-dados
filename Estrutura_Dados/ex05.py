lista = []

num = int(input("Digite um número: "))

for i in range(2, num+1):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    
    if primo:
        lista.append(i) 

print(lista)