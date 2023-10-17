def validacao_string(string, max, min):
    if len(string) < max and len(string) > min:
        print("Verdadeiro!")
    else:
        print("Falso!")


validacao_string("chuveiro", 10, 3)
validacao_string("urucubaca", 5, 1)
