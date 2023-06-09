# Dicionários - 30/05/2023

# Exemplo 1:
D = {"Lucca": [5, 7, ["Física", "Empreendedorismo", "Imposto de Renda"]]}   # criando o dicionário D
chave = "Lucca"

D[chave][2][2] = "História dos EUA"             # substituindo o valor "Imposto de Renda" por "História dos EUA"
D[chave][2].append("Química")                   # incluindo o valor "Química" no final da lista da posição 2 de D
D[chave].extend(["Shaolin matador de porco"])   # incluindo o valor "Shaolin matador de porco" no final dos valores de D
print(D[chave])                                 # mostrando todos os valores da chave "Lucca"


# Exemplo 2:
tel = {'sergio': 4139,
       'paulo': 2049,
       'anderson': 3021,
       'romeu': 4366}
print(tel)


# Exercício 1:
# Faça um programa que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ seja informado,
# após o fim da leitura, imprima o nome do aluno que possui a maior nota.
# Obs.: Use dicionário para resolver essa questão.

notas = {}
while True:
    nome = input("Digite o nome do aluno (ou 'oooo' para sair): ")
    if nome == "oooo":
        break
    nota = float(input("Digite a nota do aluno: "))
    notas[nome] = nota
print(notas)

maior_nota = 0
alunos_maior_nota = []

for x, y in notas.items():
    if y > maior_nota:
        maior_nota = y
        alunos_maior_nota.append(x)
    elif y == maior_nota:
        alunos_maior_nota.append(x)
print(f"Aluno(s) com a maior nota: {alunos_maior_nota}")


# Outra opção utilizando "get":
aluno_maior_nota = max(alunos, key=alunos.get)
print("O aluno com a maior nota é:", aluno_maior_nota)