# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# 1 Byte = 8 bits

tamanho_megabytes = float(input("Tamanho do arquivo em MB: "))
velocidade = int(input("Velocidade da internet em Mbps: "))

tamanho_megabits = tamanho_megabytes * 8
tempo = tamanho_megabits / velocidade

print(f"Tempo para realizar o download {tempo/60:.2f} minutos.")