# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.



def quadradoMagico(lista):
    linha1 = sum([lista[0], lista[1], lista[2]])
    linha2 = sum([lista[3], lista[4], lista[5]])
    linha3 = sum([lista[6], lista[7], lista[8]])

    coluna1 = sum([lista[0], lista[3], lista[6]])
    coluna2 = sum([lista[1], lista[4], lista[7]])
    coluna3 = sum([lista[2], lista[5], lista[8]])

    diagonal1 = sum([lista[0], lista[4], lista[8]])
    diagonal2= sum([lista[2], lista[4], lista[6]])

    return linha1 == linha2 == linha3 == coluna1 == coluna2 == coluna3 == diagonal1 == diagonal2


def geradorQuadrados():
    for numero1 in range(1, 10):
        for numero2 in range(1, 10):
            for numero3 in range(1, 10):
                for numero4 in range(1, 10):
                    for numero5 in range(1, 10):
                        for numero6 in range(1, 10):
                            for numero7 in range(1, 10):
                                for numero8 in range(1, 10):
                                    for numero9 in range(1, 10):
                                        lista = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8, numero9]

                                        if quadradoMagico(lista):
                                            print(lista)


geradorQuadrados()
