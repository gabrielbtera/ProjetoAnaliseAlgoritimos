
import sys
from time import  time


sys.setrecursionlimit(5000)


dic = {"HP": 0, "HM": 0, "HA": 0,
      "LP": 0, "LM": 0, "LA": 0}

def updateFlags(flag):
  global dic
  dic[flag] += 1

def trocar(lista, inicio, fim, flag):
  lista[inicio], lista[fim] = lista[fim], lista[inicio]
  updateFlags(flag)


def insertion(lista, tamanho=3):
    for step in range(1, tamanho):
        key = lista[step]
        j = step - 1
               
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        
        lista[j + 1] = key

def insertionTupla(lista, tamanho=3):
    for step in range(1, tamanho):
        key = lista[step][0]
        k2 = lista[step]
      
        j = step - 1
               
        while j >= 0 and key < lista[j][0]:
            
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = k2


def pivoMediana(i, n, lista):
  v1 = i + (n // 4)
  v2 = i + (n // 2)
  v3 = i + ((3*n) // 4)
  
  Vm = [lista[v1], lista[v2], lista[v3]]
  insertion(Vm)
  mediano = Vm[1]

  if mediano == lista[v1]:
    return v1
  elif mediano == lista[v2]:
    return v2
  elif mediano == lista[v3]:
    return v3


def pivoRandom(lista, tamanho, inicio):
  return inicio + abs(lista[inicio]) % tamanho


def quickSort(lista, inicio, fim, flag="", particao=""):
  updateFlags(flag)
    
  if inicio < fim:
    if flag == "HP" or flag == "HM" or flag == "HA":
      particao = hoare(lista, inicio, fim, flag)
      quickSort(lista, inicio, particao, flag)
      quickSort(lista, particao + 1, fim, flag)
    else:
      particao = lomuto(lista, inicio, fim, flag)
      quickSort(lista, inicio, particao-1, flag)
      quickSort(lista, particao + 1, fim, flag)

    



def lomuto(lista, inicio, fim, flag):
  global LP, LM, LA
  if flag == "LM":
   
    mediano = pivoMediana(inicio, fim - inicio + 1, lista)
    lista[fim], lista[mediano] = lista[mediano] , lista[fim]
    updateFlags(flag)
    pivot = lista[fim]
    ponto_1 = inicio
  elif flag == "LA":
    radomizado = pivoRandom(lista, fim - inicio + 1, inicio)
    updateFlags(flag)
    lista[fim], lista[radomizado] = lista[radomizado] , lista[fim]
    pivot = lista[fim]
    ponto_1 = inicio
  else:
    
    pivot = lista[fim]
    ponto_1 = inicio
  
  for ponto_2 in range(inicio, fim):
    if lista[ponto_2] <= pivot: # ordem ascendente, posso trocar para a crescente
      lista[ponto_1], lista[ponto_2] = lista[ponto_2], lista[ponto_1]
      updateFlags(flag)
      ponto_1 += 1
  
  lista[ponto_1], lista[fim] = lista[fim], lista[ponto_1]
  updateFlags(flag)

  return ponto_1


 

def hoare(lista, inicio, fim, flag=''):
    global HM, HA
    if flag == "HM":
      mediano = pivoMediana(inicio, (fim - inicio) + 1 , lista)
      lista[inicio], lista[mediano] = lista[mediano], lista[inicio]
      updateFlags(flag)
      
      pivot = lista[inicio]
      ponto_1, ponto_2 = inicio - 1, fim + 1
    elif flag == "HA":
      radomizado = pivoRandom(lista, fim - inicio + 1, inicio)
      lista[inicio], lista[radomizado] = lista[radomizado], lista[inicio]
      updateFlags(flag)
      pivot = lista[inicio]
      ponto_1, ponto_2 = inicio - 1, fim + 1
    else: 
      pivot = lista[inicio]
      ponto_1, ponto_2 = inicio - 1, fim + 1
    

    while 1:
 
      while 1:
          ponto_1 += 1
          if lista[ponto_1] >= pivot:
              break

      while 1:
          ponto_2 -= 1
          if lista[ponto_2] <= pivot:
              break

      if ponto_1 >= ponto_2:
          return ponto_2

      trocar(lista, ponto_1, ponto_2, flag)



def hoarePadrao(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "HP")
  
def hoareMediana(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "HM")


def hoareAleatorio(lista):
   tamanho = lista[0]
   subLista = lista[1]
   quickSort(subLista, 0, tamanho-1, "HA")


def lomutoPadrao(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "LP")

def lomutoMediana(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "LM")

def lomutoAleatorio(lista):
  tamanho = lista[0]
  subLista = lista[1]
  quickSort(subLista, 0, tamanho-1, "LA")


def formatarEntrada(arquivo, tamanhoTotal=0):
  tamanhoTotal = (int(arquivo[0]) - 775) * 2
  tamanho = int(arquivo[0]) - 775
  listaTuplas = []
  for indice in range(1,tamanhoTotal , 2):
    ate = int(arquivo[indice]) -1 
    listaTuplas.append([ate + 1, arquivo[indice + 1].split(" ", ate)])
  
  for dado in range(tamanho):
    listaTuplas[dado][1] = list(map(int ,listaTuplas[dado][1])) #teste
    
   
  return listaTuplas, tamanho


def formataSaida(lista, i):
  l1 = f"{i}: N({lista[0][2]}) {lista[0][1]}({lista[0][0]}) {lista[1][1]}({lista[1][0]}) {lista[2][1]}({lista[2][0]}) {lista[3][1]}({lista[3][0]}) {lista[4][1]}({lista[4][0]}) {lista[5][1]}({lista[5][0]})\n"

  return l1

# def copies(lista):
#   return {"hoareP" : lista,
#   "hoareM" : copy.deepcopy(lista),
#   "hoareA" : copy.deepcopy(lista),

#   "lomutoP" : copy.deepcopy(lista),
#   "lomutoM" : copy.deepcopy(lista),
#   "lomutoR" : copy.deepcopy(lista)
#   }

  
def menu(lista, golden, tamanho):
  global dic
  
  Hms = []
  Hps = []
  Has = []

  Lps = []
  Lms = []
  Las = []

  # copias = copies(lista)
  
  hoareP = lista["data1"][0]
  hoareM = lista["data2"][0]
  hoareA = lista["data3"][0]

  lomutoP = lista["data4"][0]
  lomutoM = lista["data5"][0]
  lomutoR = lista["data6"][0]

  for indice in hoareP:
    hoarePadrao(indice)
    Hps.append((dic["HP"], indice[0]))
    dic["HP"] = 0
  
  for indice in hoareM:
    dic["HM"] = 0
    hoareMediana(indice)
    Hms.append((dic["HM"], indice[0]))
  
  for indice in hoareA:
    dic["HA"] = 0
    hoareAleatorio(indice)
    Has.append((dic["HA"], indice[0]))

  for indice in lomutoP:
    dic["LP"] = 0
    lomutoPadrao(indice)
    Lps.append((dic["LP"] , indice[0]))
  
  for indice in lomutoM:
    dic["LM"] = 0
    lomutoMediana(indice)
    Lms.append((dic["LM"] , indice[0]))

  for indice in lomutoR:
    dic["LA"] = 0
    lomutoAleatorio(indice)
    Las.append((dic["LA"],indice[0]))

  lis = []
  for i in range(tamanho):
    l = []
    # l = [(Lps[i][0], "LP", Lps[i][1]), (Lms[i][0], "LM", Lms[i][1]), (Las[i][0], "LA", Las[i][1]), (Hps[i][0], "HP", Hps[i][1]), (Hms[i][0], "HM", Hms[i][1]), (Has[i][0], "HA", Has[i][1])]
    l = [[Lps[i][0], "LP", Lps[i][1]], [Lms[i][0], "LM", Lms[i][1]], [Las[i][0], "LA", Las[i][1]], [Hps[i][0], "HP", Hps[i][1]], [Hms[i][0], "HM", Hms[i][1]], [Has[i][0], "HA", Has[i][1]]]

    lis.append(l)

  cont = 0
  for i in lis:
    insertionTupla(i, 6)
    golden.write(formataSaida(i, cont))
    cont += 1


def main(args) -> None:
    print("#ARGS = %i"%len((args)))
    print("PROGRAMA = %s"%(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    #Abrindo Arquivos
    golden_input1 = open(sys.argv[1],'r')
    golden_input2 = open(sys.argv[1],'r')
    golden_input3 = open(sys.argv[1],'r')
    golden_input4 = open(sys.argv[1],'r')
    golden_input5 = open(sys.argv[1],'r')
    golden_input6 = open(sys.argv[1],'r')



    golden_output = open(sys.argv[2],'w')


    
    arquivo1 = golden_input1.read().split('\n')
    arquivo2 = golden_input2.read().split('\n')
    arquivo3 = golden_input3.read().split('\n')
    arquivo4 = golden_input4.read().split('\n')
    arquivo5 = golden_input5.read().split('\n')
    arquivo6 = golden_input6.read().split('\n')






    
    
    dicData = {'data1' : formatarEntrada(arquivo1),
    'data2' : formatarEntrada(arquivo2),
    'data3' : formatarEntrada(arquivo3),
    'data4' : formatarEntrada(arquivo4),
    'data5' : formatarEntrada(arquivo5),
    'data6' : formatarEntrada(arquivo6)    
    }


    

    
    menu(dicData, golden_output, dicData["data1"][1])
   

        
    #
    #fechando arquivos
    golden_input1.close()
    golden_input2.close()
    golden_input3.close()
    golden_input4.close()
    golden_input5.close()
    golden_input6.close()

    golden_output.close()
    #Finalizando programa


if __name__ == '__main__':
    main(sys.argv)
    

