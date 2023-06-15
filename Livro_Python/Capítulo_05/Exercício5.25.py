numero = float(input("Digite um número: "))
raiz = numero ** (1/2)
print(f"A raiz quadrada de {numero} é {raiz:.2f}")


# Utilizando o Método de Newton (base b=2) e a fórmula p=(b+(n/b))/2
n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")