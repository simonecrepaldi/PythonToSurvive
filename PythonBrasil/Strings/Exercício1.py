# Exercício 1 - Tamanho de strings.
# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"Primeira string: {string1} - tamanho: {len(string1)}")
print(f"Segunda string: {string2} - tamanho: {len(string2)}")

if len(string1) == len(string2):
    if string1 == string2:
        print("As strings possuem o mesmo comprimento e são iguais no conteúdo.")
    else:
        print("As strings possuem o mesmo comprimento, mas possuem conteúdos diferentes.")
else:
    print("As strings possuem conteúdos e comprimentos diferentes.")
