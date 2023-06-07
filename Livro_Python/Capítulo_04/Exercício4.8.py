# Exercício 4.8
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
oper = input("Qual operação você deseja realizar: ").lower()
if oper == 'soma':
    resultado = a + b
elif oper == 'subtração':
    resultado = a - b
elif oper == 'multiplicação':
    resultado = a * b
elif oper == 'divisão':
    resultado = a / b
else:
    print("Operação digitada inválida!")
    resultado = 'inválido'
print(f"Resultado da {oper} entre {a} e {b}: {resultado}")
