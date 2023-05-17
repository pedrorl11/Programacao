def f_inclui(d):
    l = []
    nome = input()
    tel = input()
    l.append(tel)
    r = input()
    while (r.upper() == "S"):
        tel = int(input())
        l.append(tel)
        r = input()
    if len(l) == 1:
        l = tel
    d[nome] = l
    return d

def imprime(d):
    for nome,valor in d.items():
        print(nome, valor)

def main():
    dic = {"wagner": 666, "maria": 555, "pedro": 333, "jose": 111}
    r = input()
    if (r.upper() == "S"):
        dic = f_inclui(dic)
    imprime(dic)
    return 0

if __name__ == "__main__":
    main()