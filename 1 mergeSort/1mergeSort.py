import sys

from time import time

# E = ['QOZJ7913219 34.699.211/9365-11 13822' for i in range(0, 60000)]
# print(E)
# arq = open('teste2.txt', 'w')
# for i in E:
#     arq.write(i+'\n')
# inicio = time()
# print(inicio)
# def mergeSort(lista, inicio, fim):
  
#   if (fim - inicio) > 1:
    
#     meio = (fim + inicio) // 2
#     mergeSort(lista, inicio, meio) 
#     mergeSort(lista, meio, fim) 
#     merge(lista, inicio, meio, fim) 

# def merge(lista, inicio, meio, fim):
#   left = lista[inicio: meio]
#   rigth = lista[meio: fim]
#   head_left = 0
#   head_rigth = 0

 

#   size_l =  meio -  inicio
#   size_r = fim - meio

#   for k in range(inicio, fim):
#     if head_left >= size_l:
#       lista[k] = rigth[head_rigth]
#       head_rigth += 1

#     elif head_rigth >= size_r:
#       lista[k] = left[head_left]
#       head_left += 1
#     elif left[head_left] < rigth[head_rigth]:
#       lista[k] = left[head_left]
#       head_left += 1
#     else:
#       lista[k] = rigth[head_rigth]
#       head_rigth += 1


# mergeSort(E, 0, 200000)
# # E.sort()
# fim = time()
# print('fim', fim-inicio)

# print('total', fim-inicio)

def acha_indices(arquivo) -> int:
    numero = int(arquivo[0])
    achado = int(arquivo[int(numero) + 1])
    return achado

def primeiraParte(arquivo):
    numeroPrimeira = int(arquivo[0])
    conteiners = arquivo[1: numeroPrimeira + 1]
    for conteiner in range( numeroPrimeira):
        conteiners[conteiner] = conteiners[conteiner].split(' ')
    return conteiners
    

def segundaParte(arquivo):
    numeroSegunda = int(arquivo[0]) + 1
    dicSegundo  = {}
    conteiners = arquivo[numeroSegunda + 1:]

    for conteiner in conteiners:
        splitConteiner = conteiner.split(' ')
        dicSegundo[splitConteiner[0]] = (splitConteiner[1], int(splitConteiner[2]))
    
    print(dicSegundo)
    return dicSegundo


    


def main(args) -> None:
    #Ilustrando uso de argumentos de programa
    # print("#ARGS = %i"%len((args)))
    # print("PROGRAMA = %s"%(args[0]))
    # print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))

    #Abrindo Arquivos
    golden_input = open("teste.txt", 'r')
    golden_output = open("output.txt", 'w')

    
    arquivo = golden_input.read().split('\n')
    
    

    acha_indices(arquivo)
    primeiraParteConteiners = primeiraParte(arquivo)
    segundaParteConteiners = segundaParte(arquivo)
    #
    #fechando arquivos
    golden_input.close()
    golden_output.close()
    #Finalizando programa
inicio = time()
if __name__ == '__main__':
    main(sys.argv)

fim = time()
print('fim', fim-inicio)