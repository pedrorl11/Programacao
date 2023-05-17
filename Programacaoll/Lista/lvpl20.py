def f_mediaPesoM(l,s):
    soma = 0
    cont = 0
    for i in range(len(s)):
        if (s[i] == "M"):
            soma = soma + l[i]
            cont = cont + 1
    return soma/cont

def f_maiorAlturaH(l,s):
    primeiro = True
    for i in range(len(s)):
        if (s[i] == "M"):
            if (primeiro):
                maior = l[i]
                primeiro = False
            else:
                if (l[i] > maior):
                    maior = l[i]
    return maior

def f_mediaAlturaF(l,s):
    soma = 0
    cont = 0
    for i in range(len(s)):
        if (s[i] == "F"):
            soma = soma + l[i]
            cont = cont + 1
    return soma/cont

def f_menorPesoF(l,s):
    primeiro = True
    for i in range(len(s)):
        if (s[i] == "F"):
            if (primeiro):
                menor = l[i]
                primeiro = False
            else:
                if (l[i] < menor):
                    menor = l[i]
    return menor

def f_media(l):
    soma = 0
    for i in range(len(l)):
        soma = soma + l[i]
    return soma/len(l)

def f_pesoAcima(l,s,m):
    cont = 0
    for i in range(len(s)):
        if (s[i] == "F"):
            if (l[i] > m):
                cont = cont + 1
    return cont

def f_alturaAbaixo(l,s,m):
    cont = 0
    for i in range(len(s)):
        if (s[i] == "M"):
            if (l[i] < m):
                cont = cont + 1
    return cont

def main():
    sexo = []
    altura = []
    peso = []
    for i in range(25):
        sexo.append(input())
        altura.append(float(input()))
        peso.append(float(input()))
    mediaPeso = f_media(peso)
    mediaAltura = f_media(altura)
    print(f"{f_mediaPesoM(peso,sexo):.2f}")
    print(f"{f_maiorAlturaH(altura,sexo):.2f}")
    print(f"{f_mediaAlturaF(altura,sexo):.2f}")
    print(f"{f_menorPesoF(peso,sexo):.2f}")
    print(f"{mediaPeso:.2f}")
    print(f"{mediaAltura:.2f}")
    print(f"{f_pesoAcima(peso,sexo,mediaPeso):.2f}")
    print(f"{f_alturaAbaixo(altura,sexo,mediaAltura):.2f}")
    
    return 0
if __name__=="__main__":
    main()