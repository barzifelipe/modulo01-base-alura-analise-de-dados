turno = input("Em qual turno você estuda (manhã, tarde ou noite)?").lower()

if turno == "manhã":
    print("Bom dia!")
elif turno == "tarde":
    print("Boa tarde!")
elif turno == "noite":
    print("boa noite!")
else:
    print("Opção inválida")