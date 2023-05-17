def tamanho(x):
    cont = 0
    if (x < 0):
        x = x * -1
    while(x > 0):
        x = x // 10
        cont = cont + 1
    return cont


def invert(x, y):
    cont = 0
    if x < 0:
        x = x * -1
    while x > 0:
        resto = x % 10
        cont = cont + resto * 10 ** y
        y -= 1
        x = x // 10
    return cont