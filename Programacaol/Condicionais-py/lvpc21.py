op = int(input("Informe a operação desejada 1, 2, 3, 4, 5, 6: "))
n1 = int(input("n1: "))
n2 = int(input("n2: "))
if op == 1:
    n3 = n1 + n2
    print(n3)
elif op == 2:
    n3 = n1 - n2
    print(n3)
elif op == 3:
    n3 = n1 * n2
    print(n3)
elif op == 4:
    n3 = n1 // 2
    print(n3)
elif op == 5:
    n3 = n1 ** n2
    print(n3)
elif op == 6:
    n3 = n1  ** (1/n2)
    print(n3)
elif op >= 7:
    print("OPERACAO INVALIDA")