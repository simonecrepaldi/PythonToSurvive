ultimo = 10
fila = list(range(1, ultimo +1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente na fila, ")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("operacao (F, A ou S): ").upper()

    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F":
            ultimo += 1 # Incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S")
        x += 1
    if sair:
        break
