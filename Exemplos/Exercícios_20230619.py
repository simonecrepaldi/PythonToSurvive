# Exercícios de Estruturas de Dados - 19/06/2023

# Exercício 1:
# Crie um conjunto chamado "frutas" com os nomes de algumas frutas.
# Imprima o conjunto para visualizar os elementos.
frutas = {"abacaxi", "limão", "melância", "manga", "mirtilo"}
print(frutas)


# Exercício 2:
# Crie dois conjuntos chamados "A" e "B" com alguns elementos.
# Calcule e imprima a união dos dois conjuntos.
A = {1, 6, 8, 4, 2}
B = {2, 5, 3, 7, 6}
print(A.union(B))
print(A|B)


# Exercício 3:
# Crie dois conjuntos chamados "A" e "B" com alguns elementos.
# Calcule e imprima a interseção dos dois conjuntos.
A = {1, 6, 8, 4, 2}
B = {2, 5, 3, 7, 6}
print(A.intersection(B))
print(A&B)


# Exercício 4:
# Crie um conjunto chamado "alunos" com nomes de alunos.
# Solicite ao usuário que digite o nome de um aluno e verifique se o aluno está presente no conjunto.
# Se estiver, imprima uma mensagem informando que o aluno foi encontrado;
# caso contrário, exiba uma mensagem informando que o aluno não foi encontrado.
alunos = {"Elaine", "Jerry", "George", "Kramer"}
nome = input("Informe o nome do aluno: ")
if nome in alunos:
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado!")


# Exercício 5:
# Crie um conjunto chamado "numeros" com alguns números inteiros.
# Imprima o tamanho do conjunto.
numeros = {1, 6, 8, 10, 15, 18, 23, 34}
print(f"Tamanho: {len(numeros)}")
