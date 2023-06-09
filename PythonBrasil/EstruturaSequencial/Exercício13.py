# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a altura em metros: "))
gênero = input("Informe se a pessoa é mulher (M) ou homem (H): ").upper()

if gênero == 'M':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura} m de altura é {peso_ideal:.2f}kg")
elif gênero == 'H':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura} m de altura é {peso_ideal:.2f}kg")
else:
    print("Informação inválida! Não é possível calcular o peso ideal da pessoa.")


# Considerando a opção "outros" para o gênero
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Para outros: (65.1*h) - 48.2

altura = float(input('Digite seu altura: '))
genero = input('Digite H para homem, M para mulher ou outra letra para outros: ')
if genero == 'h' or genero == 'H':
    coef1 = 72.7
    coef2 = 58
    desc = 'um homem'
elif genero == 'm' or genero == 'M':
    coef1 = 62.1
    coef2 = 44.7
    desc = 'uma mulher'
else:
    coef1 = 65.1
    coef2 = 48.2
    desc = 'alguém'
peso_ideal = (coef1 * altura) - coef2
print(f"O peso ideal para {desc} de altura {altura:.2f} m é de {peso_ideal:.2f} Kg")
