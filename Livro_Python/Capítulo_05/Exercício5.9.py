dividendo = int(input("Primeiro número: "))
divisor = int(input("Segundo número: "))
quociente = 0
resto = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"A divisão inteira de {dividendo} por {divisor} é {quociente} e o resto é {resto}")

# quociente = dividendo // divisor
# resto = dividendo % divisor

