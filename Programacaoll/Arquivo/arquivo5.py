def f_leArq():
    m = []
    arquivo = open("notas.txt", "r")
    for linha in arquivo:
        t = linha[:-1].split()
        m.append(t)
    return f_atualiza(m)

def f_atualiza(m):
    for i in range(len(m)):
        m[i][1] = float(m[i][1])
        m[i][2] = float(m[i][2])
    return m
    
def f_mpM(m):
  soma = 0
  cont = 0
  for i in range(25):
    if (m[i][0] == "M"):
      soma = soma + m[i][2]
      cont += 1
  return soma/cont

#função maior altura homens
def f_Altm(m):
  maior = 0
  for i in range(25):
    if m[i][0] == "M":
      if m[i][1] > maior:
        maior = m[i][1]
  return maior

#função média de alturas mulheres
def f_mpf(m):
  soma = 0
  cont = 0
  for i in range(25):
    if (m[i][0] == "F"):
      soma = soma + m[i][1]
      cont += 1
  return soma/cont

#função menor peso entre as mulheres
def f_menorPesoF(Ma):
    primeiro = True
    for i in range(25):
        if (Ma[i][0] == "F"):
            if (primeiro):
                menor = Ma[i][2]
                primeiro = False
            else:
                if (Ma[i][2] < menor):
                    menor = Ma[i][2]
    return menor    

#função média de peso do grupo
def f_mP(Ma):
    soma = 0
    for i in range(25):
      soma = soma + Ma[i][2]
    return soma/25

#função média de altura do grupo
def f_mAlt(Ma):
    soma = 0
    for i in range(25):
        soma = soma + Ma[i][1]
    return soma/25

#função quantidade de mulheres com peso acima da média do grupo
def f_pesoAcima(Ma,m):
    cont = 0
    for i in range(25):
        if (Ma[i][0] == "F"):
            if (Ma[i][2] > m):
                cont = cont + 1
    return cont

#função quantidade homens altura abaixo da média
def f_alturaAbaixo(Ma,m):
    cont = 0
    for i in range(25):
        if (Ma[i][0] == "M"):
            if (Ma[i][1] < m):
                cont = cont + 1
    return cont

def main():
  matriz = f_leArq()
  mediaAlt = f_mAlt(matriz)
  mediaP = f_mP(matriz)
  print(f"{f_mpM(matriz):.2f}")
  print(f"{f_Altm(matriz):.2f}")
  print(f"{f_mpf(matriz):.2f}")
  print(f"{f_menorPesoF(matriz):.2f}")
  print(f"{f_mP(matriz):.2f}")
  print(f"{f_mAlt(matriz):.2f}")
  print(f"{f_pesoAcima(matriz,mediaP):.2f}")
  print(f"{f_alturaAbaixo(matriz,mediaAlt):.2f}")
    
  return 0
if __name__=="__main__":
    main()