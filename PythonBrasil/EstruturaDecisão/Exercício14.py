# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Nota 01: "))
nota2 = float(input("Nota 02: "))
media = (nota1 + nota2)/2
conceito = 0
situacao = 0

if 9 < media <= 10:
    conceito = "A"
elif 7.5 < media <= 9:
    conceito = "B"
elif 6 < media <= 7.5:
    conceito = "C"
elif 4 < media <= 6:
    conceito = "D"
else:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media} - Conceito {conceito}")
print(f"Situação: {situacao}")