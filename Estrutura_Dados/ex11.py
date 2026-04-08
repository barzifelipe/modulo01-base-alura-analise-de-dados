total_vendas = 0
maior_valor = 0
produto_maior = ""

dados = {'Produto A': 200, 'Produto B': 80, 'Produto C': 60, 'Produto D': 300, 'Produto E': 250, 'Produto F': 30}

for produto, valor in dados.items():
    total_vendas += valor

    if valor > maior_valor:
        maior_valor = valor
        produto_maior = produto

print(f"Total de vendas: {total_vendas}")
print(f"Maior venda: {produto_maior} ({maior_valor})")