while True:
    numero = int(input("Número escolhido: "))
    print(">>> LISTA DE OPÇÕES <<<")
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Divisão")
    print("[4] - Multiplicação")
    print("[5] - Sair")

    escolha = int(input("Opção escolhida: "))
    tabuada = 1

    if escolha == 5:
        print("> > > Programa finalizado!")
        break
    else:
        while tabuada <= 10:
            if escolha == 1:
                print(f"{numero} + {tabuada} = {numero + tabuada}")
                tabuada += 1
            elif escolha == 2:
                print(f"{numero} - {tabuada} = {numero - tabuada}")
                tabuada += 1
            elif escolha == 3:
                print(f"{numero} / {tabuada} = {numero / tabuada}")
                tabuada += 1
            elif escolha == 4:
                print(f"{numero} x {tabuada} = {numero * tabuada}")
                tabuada += 1
