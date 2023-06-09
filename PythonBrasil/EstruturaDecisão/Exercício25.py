# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

x = 0
print("> > > > > INTERROGATÓRIO! < < < < <")
print("Pergunta 1: Telefonou para a vítima?")
resposta = input("Resposta (S / N): ").upper()
if resposta == "S":
    x +=1
print("Pergunta 2: Esteve no local do crime?")
resposta = input("Resposta (S / N): ").upper()
if resposta == "S":
    x +=1
print("Pergunta 3: Mora perto da vítima?")
resposta = input("Resposta (S / N): ").upper()
if resposta == "S":
    x +=1
print("Pergunta 4: Devia para a vítima?")
resposta = input("Resposta (S / N): ").upper()
if resposta == "S":
    x +=1
print("Pergunta 5: Já trabalhou com a vítima?")
resposta = input("Resposta (S / N): ").upper()
if resposta == "S":
    x +=1
print()
print(f"Você respondeu SIM para {x} perguntas.")
if x == 2:
    print("Você é um dos suspeitos!")
elif x == 3 or x == 4:
    print("Você é cúmplice do crime!")
elif x == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente!")