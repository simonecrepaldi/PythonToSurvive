# Validador de CPF
# A fórmula para validar um CPF é a seguinte: Separe os 9 primeiros dígitos do CPF em um vetor;
# 1. Calcule o primeiro dígito verificador utilizando o seguinte algoritmo:
# 1.1. Multiplique cada dígito do vetor pela sequência de pesos 10, 9, 8, 7, 6, 5, 4, 3, 2, da esquerda para a direita;
# 1.2. Some os resultados das multiplicações;
# 1.3. Calcule o resto da divisão da soma por 11;
# 1.4. Se o resto for menor que 2, o primeiro dígito verificador será 0, caso contrário, subtraia o resto de 11.
# 2. Cálculo do segundo dígito verificador:
# 2.2 Pegue os primeiros 10 dígitos do CPF (incluindo o primeiro dígito verificador obtido anteriormente) e multiplique cada um por um peso que varia de 11 a 2.
# 2.3 Some os resultados das multiplicações.
# 2.4 Calcule o resto da divisão da soma por 11.
# 2.5 Se o resto for menor que 2, o segundo dígito verificador é 0. Caso contrário, subtraia o resto de 11.
# 2.6 Se os dois dígitos verificadores calculados forem iguais aos dois últimos dígitos do CPF, então o CPF é válido.

str_cpf = input("Digite o CPF: ")
semponto = str_cpf.replace(".", "")
cpf = semponto.replace("-", "")

L = list(cpf)
L.pop()
L.pop()
peso1 = 10
x = 0
soma = 0
while x <= 8:
  num = int(L[x])
  mult = num * peso1
  soma += mult
  peso1 -= 1
  x += 1
print(soma)

resto = soma%11
if resto < 2:
  pdv = 0
else:
  pdv = 11 - resto

numero = str(pdv)
L.append(numero)

peso2 = 11
y = 0
soma2 = 0
while y <= 9:
  num = int(L[y])
  mult = num * peso2
  soma2 += mult
  peso2 -= 1
  y += 1

resto2 = soma2%11
if resto2 < 2:
  sdv = 0
else:
  sdv = 11 - resto2

L = list(cpf)

print(L[9])
print(pdv)
print(L[10])
print(sdv)

if pdv == int(L[9]) and sdv == int(L[10]):
  print("CPF válido!")
else:
  print("CPF inválido!")
