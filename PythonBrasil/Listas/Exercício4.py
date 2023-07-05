# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

tamanho = 10
vetor = []
consoantes = []
for letras in range(tamanho):
    vetor.append(input("Digite um caractere: "))
for caractere in vetor:
    if caractere.isalpha() and caractere not in "aeiou":
        consoantes.append(caractere)
print(f"Temos {len(consoantes)} consoantes: {consoantes}")
