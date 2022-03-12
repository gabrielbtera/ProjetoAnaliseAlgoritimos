import sys

def primeiraParte(arquivo):
    numeroPrimeira = int(arquivo[0])
    conteiners = arquivo[1: numeroPrimeira + 1]
    for conteiner in range( numeroPrimeira):
        conteinerPronto = conteiners[conteiner].split(' ')
        conteiners[conteiner] = [conteinerPronto[0], conteinerPronto[1], int(conteinerPronto[2])]
    return conteiners
    

def segundaParte(arquivo):
    numeroSegunda = int(arquivo[0]) + 2

    dicSegundo  = {}
    conteiners = arquivo[numeroSegunda :]
    for conteiner in conteiners:
        if conteiner != '':
            splitConteiner = conteiner.split(' ')
            dicSegundo[splitConteiner[0]] = (splitConteiner[1], int(splitConteiner[2]))
    return dicSegundo

def percentuaDedoisnumeros(numero1, numero2):
    if numero1 > numero2:
        return round(((numero1 - numero2) / numero2) * 100), numero1 - numero2

    return round(((numero2 - numero1) / numero1) * 100), numero2 -numero1


def ordenaPeloCNPJEextraipercentual(listaPivo, dicAnalisado):
    lista = []
    lista2 = []
    contador1 = 0
    contador2 = 0
    for conteinerPivot  in listaPivo:
        conteinerAnalisado = dicAnalisado.get(conteinerPivot[0])
        if (conteinerAnalisado):
            percentualPeso, diferenca = percentuaDedoisnumeros(conteinerAnalisado[1], conteinerPivot[2])
            if (conteinerAnalisado[0] != conteinerPivot[1]):
                lista.append([conteinerPivot[0],conteinerPivot[1], conteinerAnalisado[0], conteinerAnalisado[1]])
                contador1 += 1
            elif (percentualPeso > 10):
                lista2.append([conteinerPivot[0], conteinerAnalisado[0], percentualPeso, diferenca])
                contador2 += 1

    lista = lista + lista2
    return lista, contador1, contador2



def mergeSort(lista, inicio, fim):
    if (fim - inicio) > 1:
        meio = (fim + inicio) // 2
        mergeSort(lista, inicio, meio) 
        mergeSort(lista, meio, fim) 
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio: meio]
    rigth = lista[meio: fim]
    head_left = 0
    head_rigth = 0

    size_l =  meio -  inicio
    size_r = fim - meio

    for k in range(inicio, fim):
        if head_left >= size_l:
            lista[k] = rigth[head_rigth]
            head_rigth += 1

        elif head_rigth >= size_r:
            lista[k] = left[head_left]
            head_left += 1
        elif left[head_left][2] < rigth[head_rigth][2]:
            lista[k] = rigth[head_rigth]
            head_rigth += 1
        else:
            lista[k] = left[head_left]
            head_left += 1


                    
def main(args) -> None:
    
    print("#ARGS = %i"%len((args)))
    print("PROGRAMA = %s"%(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    #Abrindo Arquivos
    golden_input = open(sys.argv[1],'r')
    golden_output = open(sys.argv[2],'w')

    
    arquivo = golden_input.read().split('\n')

    primeiraParteConteiners = primeiraParte(arquivo)
    segundaParteConteiners = segundaParte(arquivo)

    dados = ordenaPeloCNPJEextraipercentual(primeiraParteConteiners, segundaParteConteiners)

    listaAtualizada = dados[0]
    inicio, fim = dados[1] , dados[1] + dados[2]

    
    mergeSort(listaAtualizada, inicio, fim)

    for indiceDado in range(fim):
        if indiceDado >= inicio:
            conteiner = listaAtualizada[indiceDado]
            golden_output.write(f'{conteiner[0]}: {conteiner[3]}Kg ({conteiner[2]}%)\n')

        else:
            conteiner = listaAtualizada[indiceDado]
            golden_output.write(f'{conteiner[0]}: {conteiner[1]}<->{conteiner[2]}\n')

        
    #
    #fechando arquivos
    golden_input.close()
    golden_output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)

