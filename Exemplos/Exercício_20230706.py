# Função para verificar se um número é primo
def primo(p):
    if p == 2 or p == 1:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, p):
        if p % i == 0:
            return False
    return True

print(primo(0))
print(primo(1))
print(primo(2))
print(primo(5))
print(primo(8))
print(primo(13))
print(primo(27))
print(primo(33))
print(primo(50))
print(primo(79))
