# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random
def embaralhar(palavra):
  letras = list(palavra)
  random.shuffle(letras)
  nova_palavra = "".join(letras)
  return nova_palavra


palavra = input("Digite uma palavra: ").upper()
print(embaralhar(palavra))

