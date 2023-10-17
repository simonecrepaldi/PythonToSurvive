def mdc(a, b):
    if b == 0:
        return a
    if a > b:
        return mdc(b, a % b)
    else:
        return mdc(a, b % a)


print(f"{mdc(40, 60)}")
