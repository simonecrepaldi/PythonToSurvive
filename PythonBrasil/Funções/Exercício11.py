# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def converter(data):
  nova_data = data.split("/")
  dia = int(nova_data[0])
  mes = int( nova_data[1])
  ano = int(nova_data[2])
  lista_meses = ['janeiro', 'fevereiro', 'março',
         'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro']

  if dia < 1 or dia > 31:
    return "Data inválida!"
  elif  mes < 1 or mes > 12:
    return "Data inválida!"
  elif ano < 0:
    return "Data inválida!"
  else:
    return f"{dia} de {lista_meses[mes-1]} de {ano}"


data_atual = input("Digite a data (DD/MM/AAAA): ")
print(converter(data_atual))


# outra forma de resolver usando um dicionário
def converter(data):
  nova_data = data.split("/")
  dia = int(nova_data[0])
  mes = int( nova_data[1])
  ano = int(nova_data[2])
  lista_meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março',
         4: 'abril', 5: 'maio', 6: 'junho',
         7: 'julho', 8: 'agosto', 9: 'setembro',
         10: 'outubro', 11: 'novembro', 12: 'dezembro'}

  if dia < 1 or dia > 31:
    return "Data inválida!"
  elif  mes < 1 or mes > 12:
    return "Data inválida!"
  elif ano < 0:
    return "Data inválida!"
  else:
    return f"{dia} de {lista_meses[mes]} de {ano}"


data_atual = input("Digite a data (DD/MM/AAAA): ")
print(converter(data_atual))