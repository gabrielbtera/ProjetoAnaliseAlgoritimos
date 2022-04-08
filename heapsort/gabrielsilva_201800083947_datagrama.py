import sys



def lerEntrada(arquivo) -> tuple:
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


def ordenaUDPPacotes(lista, tamanho, intervalo, dicionario) -> list:
  
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
   

    
    pilha = inserirNoMaior(pilha)
    while sequencia in pilha :
      if pilha[cont] == sequencia:
        linha.append(dicionario[pilha[cont]][1]) 
        sequencia += 1
        del[pilha[cont] ]
        contPilha -= 1
        cont -= 1
      cont += 1
    if linha != []:
      listaImprimir.append(linha)
    linha = []
    cont1 += 1


  return listaImprimir
      

def inserirNoMaior(lista) -> list:
  return sorted(lista)

def imprimirTxt(lista, arquivo) -> None:
  cont = 0
  
  for i in lista:
    arquivo.write(f"{cont}: ")

    for st in i:
      arquivo.write(f"{st} ")
    arquivo.write("\n")
    cont += 1

def main(args) -> None:
    print("#ARGS = %i"%len((args)))
    print("PROGRAMA = %s"%(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    
    golden_input = open(sys.argv[1],'r')
    golden_output = open(sys.argv[2],'w')

    arquivo = golden_input.read().split('\n')
    dicionarioPacotes, indicesPacotes, intervaloPacotes, numeroTotalPacotes = lerEntrada(arquivo)

  
    listaImprimir = ordenaUDPPacotes(indicesPacotes, numeroTotalPacotes, intervaloPacotes, dicionarioPacotes)
    imprimirTxt(listaImprimir, golden_output)
  
    
    golden_input.close()
    golden_output.close()




if __name__ == '__main__':
  main(sys.argv)



