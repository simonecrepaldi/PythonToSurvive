# Obtenção do preço com um dicionário

estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
            "feijão": [100, 1.50]}
total = 0
venda =[]

while True:
    produto = input("Digite o nome do produto, fim para terminar: ").lower()
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade <= estoque[produto][0]:
            venda.append([produto, quantidade])
        else:
            print("Quantidade indisponível no estoque. Produto não adicionado.")
    else:
        print("Produto não encontrado!")

print("Vendas: \n")
for operacao in venda:
    produto, quantidade = operacao
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo total: R${total:21.2f}\n")

print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
