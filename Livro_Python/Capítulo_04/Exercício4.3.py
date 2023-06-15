# Exercício 4.3
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
if a > b > c:
    print(f"O maior número é o {a} e o menor é {c}")
if a > c > b:
    print(f"O maior número é o {a} e o menor é {b}")
if b > c > a:
    print(f"O maior número é o {b} e o menor é {a}")
if b > a > c:
    print(f"O maior número é o {b} e o menor é {c}")
if c > a > b:
    print(f"O maior número é o {c} e o menor é {b}")
if c > b > a:
    print(f"O maior número é o {c} e o menor é {a}")
