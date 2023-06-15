a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
x = 1
resultado = 0

while x <= b:
    resultado = resultado + a
    x += 1
print(f">>>> {a} x {b} = {resultado}")
