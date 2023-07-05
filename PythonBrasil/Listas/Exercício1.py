# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
tamanho = 5
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

print("Números digitados: ")
for numero in vetor:
    print(numero)
    