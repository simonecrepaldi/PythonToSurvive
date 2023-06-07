tabuada = 1
while tabuada <= 10:
    número = 1
    while número <= 10:
        print(f"{tabuada} x {número} = {tabuada * número}")
        número += 1
    tabuada += 1

print()

tabuada = 1
número = 1
while tabuada <= 10:
    print(f"{tabuada} x {número} = {tabuada * número}")
    número += 1
    if número == 11:
        número = 1
        tabuada += 1

