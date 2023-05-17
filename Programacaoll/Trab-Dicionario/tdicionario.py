def f_leArq():
    arquivo = open("notas.txt","r")
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
    
def f_imprime(d):
    for i in d:
        print (i)
    
def imprime(d):
    for nome,valor in d.items():
        print(nome, valor)

def main():
    dic = f_imprime(f_leArq())
    r = input()
    if (r.upper() == "S"):
        dic = f_inclui(dic)
    imprime(dic)
    return 0

if __name__ == "__main__":
    main()