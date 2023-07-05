# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

tamanho = 10
vetor = []
for i in range(tamanho):
    numero = float(input("Digite um número inteiro: "))
    vetor.append(numero)
for x in range(tamanho-1, -1, -1):
    print(vetor[x])

# tamanho-1 = vai começar a mostrar o valor na posição 9
# -1 = vai até o valor na posição 0
