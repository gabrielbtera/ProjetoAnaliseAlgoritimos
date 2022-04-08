# from msilib import sequence

from time import time

import timsort
import cProfile

  





def heapify(arr, n, i):
    
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2  
  
  
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
        heapify(arr, n, largest)

def heapsort(arr, n):
    
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
  



# print(lista)

def lerEntrada(arquivo):
  linha1 = arquivo[0].split(" ")
  numeroTotalPacotes = int(linha1[0])
  intervaloPacotes = int(linha1[1])
  dicionarioDados = {}
  indicesPacote = []
  

  for pacote in range(1, numeroTotalPacotes + 1):
   
    quebrar = arquivo[pacote].split(" ")
    numeroPacote = int(quebrar[0])
    tamanhoPacote = int(quebrar[1]) 
    conteudo = ' '.join(quebrar[2: tamanhoPacote + 2])

  
    
  
    indicesPacote.append(numeroPacote)
    
    dicionarioDados[numeroPacote] = (tamanhoPacote, conteudo)
  
  return dicionarioDados, indicesPacote, intervaloPacotes, numeroTotalPacotes
  




def ordenarIntervalo(lista, intervalo,tamanho) -> list:
  listaIntervalos = []
  
  # print(lista)
  # print(nItervalo)
  it = 0
  listaTemp = []
  for i in range(tamanho):
    if it == intervalo:
      it = 0
      listaIntervalos.append(listaTemp)
      listaTemp = []

    listaTemp.append(lista[i])
    it += 1

  
  listaIntervalos.append(listaTemp)
  return listaIntervalos



    

def ordenaPacotes(lista, tamanho, intervalo, dicionario):
  
  pilha = []
  listatemp = []
  sequencia = 0

  listaImprimir = []
  cont1 = 0
  
  

  contPilha = 0
  for pacotes in range(0, tamanho, intervalo):
    if pacotes == 0:
      listatemp = lista[: intervalo]
    else:
      listatemp = lista[pacotes: pacotes + intervalo]

    cont = 0
    linha = []
    
    for pacote in listatemp:
      if pacote == sequencia and pilha == []:
        sequencia += 1
        linha.append(dicionario[pacote][1])
      else:

        # inserirNoMaior(pilha, pacote,  contPilha)
        contPilha += 1
        pilha.append(pacote)
        
      cont += 1
    
    cont = 0
    if linha != []:
      listaImprimir.append(linha)
    linha = []
   

    
    pilha = sorted(pilha)
    while sequencia in pilha :
      if pilha[cont] == sequencia:
        linha.append(dicionario[pilha[cont]][1]) 
        sequencia += 1
        del[pilha[cont]]
        contPilha -= 1
        cont -= 1
      cont += 1
    if linha != []:
      listaImprimir.append(linha)
    linha = []
    cont1 += 1
  return listaImprimir
      

def inserirNoMaior(lista, valor, tamanho):
  for i in range(tamanho):
    if lista[i] > valor:
      temp = lista[i]
      lista[i] = valor
      valor = temp

  lista.append(valor)


def imprimirTxt(lista, arquivo):
  cont = 0
  
  for i in lista:
    arquivo.write(f"{cont}: ")

    for st in i:
      arquivo.write(f"{st} ")
    arquivo.write("\n")
    cont += 1









def main(args = None) -> None:
    #Ilustrando uso de argumentos de programa
    # print("#ARGS = %i"%len((args)))
    # print("PROGRAMA = %s"%(args[0]))
    # print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))

    #Abrindo Arquivos
    golden_input = open("datagrama.input.txt", 'r')
    golden_output = open("output.txt", 'w')
    arquivo = golden_input.read().split('\n')
    dicionarioPacotes, indicesPacotes, intervaloPacotes, numeroTotalPacotes = lerEntrada(arquivo)

    # print(indicesPacotes)
    # heapsort(indicesPacotes)
    # print(indicesPacotes)

    # heapsort(indicesPacotes, golden_output)

    # lista = ordenarIntervalo(indicesPacotes, dicionarioPacotes.keys(), numeroTotalPacotes)
    # # print(lista)
    
    listaImprimir = ordenaPacotes(indicesPacotes, numeroTotalPacotes, intervaloPacotes, dicionarioPacotes)
    imprimirTxt(listaImprimir, golden_output)
  
        
    #
    #fechando arquivos
    golden_input.close()
    golden_output.close()

inicio = time()
 
if __name__ == '__main__':
    cProfile.run('main()')

fim = time()

print("fim", fim - inicio)

