# Programa 8.5 - Função recursiva do fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(1))
print(fatorial(0))
print(fatorial(3))
print(fatorial(5))
