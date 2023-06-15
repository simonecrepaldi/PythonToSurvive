dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resto = 0
quociente = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente += 1
resto = x

print(f"Resto = {resto}")
