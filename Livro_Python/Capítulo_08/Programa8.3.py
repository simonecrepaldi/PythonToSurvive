# Programa 8.3 - Cálculo do fatorial
def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


print(fatorial(3))
print(fatorial(0))
print(fatorial(5))
