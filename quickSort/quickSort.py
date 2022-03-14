import sys
from time import time

HP = 0
HM = 0


def trocar(lista, inicio, fim):
  global HP, HM
  lista[inicio], lista[fim] = lista[fim], lista[inicio]
  HP += 1
  HM += 1

def pivoMediana(n):
  v1 = n // 4
  v2 = n // 2
  v3 = (3*n) // 4
  return mediana(v1, v2, v3)

def pivoRandom(lista, tamanho, inicio):
  return lista[inicio + abs(lista[inicio]) % tamanho]

def mediana(n1, n2, n3):
  n = ''
 
  if (n1 >= n2 >= n3):
    n = n2
  elif (n2 >= n1 >= n3):
    n = n1
  elif (n1 >= n3 >= n2):
    n = n3

  elif (n1 <= n2 <= n3):
    n = n2
  elif (n2 <= n1 <= n3):
    n = n1
  elif (n1 <= n3 <= n2):
    n = n3
  print("v", n)
  return n



def quickSort(lista, inicio, fim, flag="", particao=""):
  global HP, HM
  if flag == "HP":
    HP += 1
  elif flag == "HM":
    HM += 1


  if inicio < fim:
    particao = hoare(lista, inicio, fim, flag)

    quickSort(lista, inicio, particao, flag)
    quickSort(lista, particao + 1, fim, flag)

def lomuto(lista, inicio, fim):
  pivot = lista[fim]
  ponto_1 = inicio

  for ponto_2 in range(inicio, fim):
    if lista[ponto_2] >= pivot: # ordem ascendente, posso trocar para a crescente
      lista[ponto_1], lista[ponto_2] = lista[ponto_2], lista[ponto_1]
      ponto_1 += 1
  
  lista[ponto_1], lista[fim] = pivot, lista[ponto_1]

  return ponto_1


 

def hoare(lista, inicio, fim, flag):
    if flag == "HM":
      mediano = pivoMediana(fim)
      print('mediano', lista)
      print("-----------------\n", lista[inicio], lista[mediano])
      print('indices', inicio, mediano)
      if mediano > inicio:
        lista[inicio], lista[mediano] = lista[mediano], lista[inicio]
      print("ourto  ", lista)
      print("-----------------\n", lista[inicio], lista[mediano])
      pivot = lista[inicio]
      ponto_1, ponto_2 = inicio - 1, fim + 1
    else: 
      pivot = lista[inicio]
      ponto_1, ponto_2 = inicio - 1, fim + 1
 
    while True:
 
      while True:
          ponto_1 += 1
          if lista[ponto_1] >= pivot:
              break

      while True:
          ponto_2 -= 1
          if lista[ponto_2] <= pivot:
              break

      if ponto_1 >= ponto_2:
          print("ponto", lista[ponto_1], lista[ponto_2] )
          return ponto_2

      trocar(lista, ponto_1, ponto_2)



def hoarePadrao(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "HP")

def hoareMediana(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "HM")


def formatarEntrada(arquivo, tamanhoTotal=0):
  tamanhoTotal = int(arquivo[0]) * 2
  tamanho = int(arquivo[0])
  listaTuplas = []
  for indice in range(1,tamanhoTotal , 2):
    listaTuplas.append([int(arquivo[indice]), arquivo[indice + 1].split(" ")])
  
  for dado in range(tamanho):
    listaTuplas[dado][1] = list(map(int ,listaTuplas[dado][1]))
  return listaTuplas

    
  
def menu(lista):

  for indice in lista:
    hoareMediana(indice)
    print(HM)
    break
    
    

    








def main(args) -> None:
    #Ilustrando uso de argumentos de programa
    # print("#ARGS = %i"%len((args)))
    # print("PROGRAMA = %s"%(args[0]))
    # print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))

    #Abrindo Arquivos
    golden_input = open("entrada.txt", 'r')
    golden_output = open("output.txt", 'w')

    
    arquivo = golden_input.read().split('\n')

    dados = formatarEntrada(arquivo)
    print(dados)
    menu(dados)
    print(dados)

        
    #
    #fechando arquivos
    golden_input.close()
    golden_output.close()
    #Finalizando programa
inicio = time()


if __name__ == '__main__':
    main(sys.argv)
meio = time()

print("fim", meio - inicio)