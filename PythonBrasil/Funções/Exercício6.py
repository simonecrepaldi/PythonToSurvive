# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def conversaoHora(hora, minuto):
    if hora >= 12:
        AMPM = "P.M."
        if hora > 12:
            hora -= 12
    else:
        AMPM = "A.M."
    return impressao(hora, minuto, AMPM)

def impressao(hora, minuto, AMPM):
    print(f"{hora}:{minuto} {AMPM}")


conversaoHora(12, 30)
conversaoHora(18, 30)
conversaoHora(3, 30)
