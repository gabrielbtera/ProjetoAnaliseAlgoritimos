import sys

import time



inicio = time.time()


def converterEmInteiro(string):
  return int(string.split(' ')[1])

def formatarEntrada(listaArquivo):
  quantidadeInteracao = int(listaArquivo[0])
  quantidadeLinhaPrimeiraMatriz =  int(listaArquivo[1].split(' ')[1])

  linhaColuna1 = listaArquivo[1].split(" ")
  qntLinha = int(linhaColuna1[1])
  quantidadeColuna = int(linhaColuna1[0])

  listaArquivo = listaArquivo[2:]
  listaMatrizes = []
  temp = 0 

  for indice in range(quantidadeInteracao):

    dictMatriz = {"Matriz": [], "Posix": (), "laterais": (quantidadeColuna, qntLinha)}

    cont = 0
    for linhaMatriz in range(temp, quantidadeLinhaPrimeiraMatriz):
      linha = listaArquivo[linhaMatriz].split(" ")
      dictMatriz["Matriz"].append(linha)
      if "X" in linha:
        dictMatriz["Posix"] = (cont, linha.index("X")) 
      cont += 1
    
    listaMatrizes.append(dictMatriz)

    temp = linhaMatriz + 2

    

    if indice < quantidadeInteracao -1 :

      linhaColuna = listaArquivo[linhaMatriz + 1].split(" ")
      qntLinha = int(linhaColuna[1])
      quantidadeColuna = int(linhaColuna[0])

      quantidadeLinhaPrimeiraMatriz = converterEmInteiro(listaArquivo[linhaMatriz + 1]) + temp

  return listaMatrizes



def escreveTransicao(arquivo, opcao, posicao1, posicao2, direcao):
  arquivo.write(f"{opcao}@{posicao1[0]},{posicao1[1]}->{posicao2[0]},{posicao2[1]}\n")
  
    


def checaPosicoes(posicao, matriz):
  coluna = posicao[1]
  linha = posicao[0]

  # print(coluna)

  if matriz[linha][coluna + 1] == "0":
    matriz[linha][coluna + 1] = "."
    # print("D")
    return (1, "D", linha, coluna + 1)

  if matriz[linha - 1][coluna] == "0":
    matriz[linha - 1][coluna] = '.'
    # print("F")
    return (1, "F", linha - 1, coluna)

  if matriz[linha][coluna - 1] == "0":
    matriz[linha][coluna - 1] = '.'
    # print("E")
    return (1, "E", linha, coluna - 1)
 
  if matriz[linha + 1][coluna] == "0":
    matriz[linha + 1][coluna] = '.'
 
    return (1, "T", linha + 1, coluna)
  
  else:
    matriz[linha][coluna] = 'b'
    return (0, "B", posicao)



def verificaBackTraking(matriz, arquivoSaida):

  contLabirinto = 0
  for cada in matriz:
    flag = 1
    arquivoSaida.write(f"L{contLabirinto}:\n")
   

    passos = []
    Matriz = cada['Matriz']
    posicao = cada['Posix']
    posicaoInicial = posicao
    fimLinha = cada['laterais']
    passos.append(posicao)
    arquivoSaida.write(f"INICIO@{posicaoInicial[0]},{posicaoInicial[1]}\n")

    

    contadorPassos = 0

    while flag:
      # print("aqui")

      
      temp = checaPosicoes(posicao, Matriz)
      

      if temp[0]:

        col = temp[3]
        linha = temp[2]
        opcaoDada = temp[1]
        posicaoAnterior = posicao
        posicao = (linha, col)

        # print(posicaoAnterior, posicao)
        escreveTransicao(arquivoSaida, opcaoDada, posicaoAnterior, posicao, 1)

        passos.append(posicao)
        contadorPassos += 1
      

        if col == fimLinha[0] -1  or linha == fimLinha[1] - 1 or col == 0 or  linha == 0:
          # print("achou fim", col, linha)
          arquivoSaida.write(f"SAIDA@{posicao[0]},{posicao[1]}\n")
          flag = 0
          

      else:
      # backtracking
        # for posicao in passos:
        if posicaoInicial == posicao and not checaPosicoes(posicao, Matriz)[0]:
          # print("não achou fim", posicao)
          arquivoSaida.write("SEM_SAIDA\n")
          flag = 0
        
        else:

          if passos != []:
            posicaoAnterior = passos[-1]
            del passos[-1]
            if passos != []:
              posicao = passos[-1]
              # print("B")
              arquivoSaida.write(f"BT@{posicao[0]},{posicao[1]}<-{posicaoAnterior[0]},{posicaoAnterior[1]}\n")

            
              # print(posicao, posicaoAnterior)
          

       
    contLabirinto += 1
 





    





    
  

def main(args):
  #   #Ilustrando uso de argumentos de programa
  #   print("#ARGS = %i"%len((args)))
  #   print("PROGRAMA = %s"%(args[0]))
  #   print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
  #  # Abrindo Arquivos
    golden_input = open(sys.argv[1],'r')
    golden_output = open(sys.argv[2],'w')

    arquivoLinhas = [i.rstrip("\n") for i in golden_input.readlines()]
    matrizes = formatarEntrada(arquivoLinhas)

    verificaBackTraking(matrizes, golden_output)

    # arquivoEntrada = open("labirinto.input2.txt", "r")
    # arquivoSaida = open("saida.txt", "w")
    # arquivoLinhas = [i.rstrip("\n") for i in arquivoEntrada.readlines()]
    # matrizes = formatarEntrada(arquivoLinhas)

    # verificaBackTraking(matrizes, arquivoSaida)


    #
    # ...
    #
    #fechando arquivos
    golden_input.close()
    golden_output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)



print("Temp", time.time() - inicio)