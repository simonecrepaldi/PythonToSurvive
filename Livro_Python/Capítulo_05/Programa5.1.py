valor = int(input("Digite o valor a pagar: R$"))
cédulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f"{cédulas} cédula(s) de R${atual}")
        if apagar ==0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0

# Exercício 5.16
# valor = 501
# 10 cédula(s) de R$50
# 0 cédula(s) de R$20
# 0 cédula(s) de R$10
# 0 cédula(s) de R$5
# 1 cédula(s) de R$1

# valor = 745
# 14 cédula(s) de R$50
# 2 cédula(s) de R$20
# 0 cédula(s) de R$10
# 1 cédula(s) de R$5

# valor = 384
# 7 cédula(s) de R$50
# 1 cédula(s) de R$20
# 1 cédula(s) de R$10
# 0 cédula(s) de R$5
# 4 cédula(s) de R$1

# valor = 2
# 0 cédula(s) de R$50
# 0 cédula(s) de R$20
# 0 cédula(s) de R$10
# 0 cédula(s) de R$5
# 2 cédula(s) de R$1

# valor = 7
# 0 cédula(s) de R$50
# 0 cédula(s) de R$20
# 0 cédula(s) de R$10
# 1 cédula(s) de R$5
# 2 cédula(s) de R$1

# valor = 1
# 0 cédula(s) de R$50
# 0 cédula(s) de R$20
# 0 cédula(s) de R$10
# 0 cédula(s) de R$5
# 1 cédula(s) de R$1

# Exercício 5.17
# valor = 0
# 0 cédula(s) de R$50