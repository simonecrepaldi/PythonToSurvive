# Exercídio 3.4
salário > 1200

# Exercício 3.5
a > b and c or d

a = 1
b = 2
c = true
d = false
resultado: false and true or false = false or false = false

a = 10
b = 3
c = false
d = false
resultado: true and false or false = false or false = false

a = 5
b = 1
c = true
d = true
resultado: true and true or true = true or true = true

# Exercício 3.6
aprovado = (matéria1 + matéria2 + matéria 3)/3 > 7

# Exercício 3.7
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = a + b
print(f"{a} + {b} = {soma}")

# Exercício 3.8
x = int(input("Digite o valor em metros: "))
y = x * 1000
print(f"{x} metro(s) equivale a {y} milímetros")

# Exercício 3.9
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)
print(total)

# Exercício 3.10
salário = float(input("Digite o salário: R$"))
aumento = float(input("Digite a % de aumento: "))
novosalario = salário * (1 + (aumento / 100))
print(f"R${novosalario:.2f}")

# Exercício 3.11
preço = float(input("Preço da mercadoria: R$"))
desconto = float(input("Desconto em %: "))
valordesconto = preço * (desconto / 100)
preçofinal = preço - valordesconto
print(f"O desconto será de R${valordesconto:.2f} e você deverá pagar R${preçofinal:.2f}")

# Exercício 3.12
x = float(input("Qual a distância a ser percorrida em km: "))
v = int(input("Qual a velocidade média esperada em km/h: "))
tempo = x / v
print(f"A viagem de {x}km feita a {v}km/h irá durar {tempo} horas")

# Exercício 3.13
c = float(input("Digite a temperatura em graus Celsius: "))
f = ((9 * c) / 5) + 32
print(f"A temperatura de {c}ºC equivale a {f}ºF.")

# Exercício 3.14
x = int(input("Qual a km percorrida: "))
d = int(input("Quantidade de dias: "))
preco = (60 * d) + (0.15 * x)
print(f"Total a ser pago será R${preco}")

# Exercício 3.15
cigarros = int(input("Quantidade de cigarros fumados por dia: "))
anos = int(input("Fumante a quantos anos: "))
cigarrostotal = (cigarros * 365 * anos)
minutosperdidos = cigarrostotal * 10
diasperdidos = minutos / 1440
print(f"O fumante perderá {diasperdidos:.1f} dias")
