from audioop import reverse
from copy import deepcopy
from math import ceil
import time




inicio = time.time()

arquivo = open('entrada.txt', 'r')
arquivoSaida = open('saida.txt', 'w')


lista = arquivo.readlines()

teste = [i.rstrip('\n') for i in lista]

tamVeiculos = 0
tamItens = 0


intervalo = int(teste[0])
listaVeiculos = []
for i in range(1, intervalo + 1):
    quebrado = teste[i].split(' ')
    tamVeiculos += 3
    dic = {}
    dic = {
            "peso":  int(quebrado[1]),
            "volume": int(quebrado[2]),
            "placa": quebrado[0]
        }

    listaVeiculos.append(dic)

# print(listaVeiculos)


intMercadoria = int(teste[intervalo + 1])


listaItens = []
listaItensCopia = []

for t in range(intervalo +2 , intervalo + 2+ intMercadoria):
    quebrado = teste[t].split(' ')
    tamItens += 4
    dic = {}

    dic = {"valor":  float(quebrado[1]), 
            "peso":  int(quebrado[2]),
            "volume": int(quebrado[3]), 
            'SuaChave':quebrado[0]}

    listaItens.append(dic)

listaItens = sorted(listaItens, key= lambda item: item['valor'], reverse=True)

listaItensCopia = deepcopy(listaItens)






def knapSack(W, wt, val, n, opcao):

    
    K = [[0] * (W + 1) for _ in range(n + 1)]

    

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w and val[i-1][opcao] >= 0:
                K[i][w] = max(val[i-1][opcao] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    i = n
    j = W
    lista = []

    while 1:
        if i-1 >=0 and K[i][j] != K[i-1][j]:
            lista.append(i-1)
            i -= 1
            j = j - wt[i]
        else:
            i-= 1
        if (i < 0 and K[i] [j] == K[i-1] [j]):
            break
  
    return lista[::-1]
  

def setta_1(lista, listaItem, flag):
    for indice in lista:
        listaItem[indice][flag] = -1

def intersecao(pesos, volume, pendentes, naoPendentes):
    lista = []

    for i in pesos:
        if i in volume:
            lista.append(i)
            naoPendentes.append(i)
        else:
            pendentes.append(i)
    
    return lista

def retornaDicionario(valores,listaItensCopia):
    return [listaItensCopia[i] for i in valores]
        

def porcentagem(cap, uni):
    return ceil(((uni/cap) * 100))
        

def verificaPesos(listaVeiculos, listaItens, listaItensCopia):
    pesosPeso = [i['peso'] for i in listaItens]
    pesosVolume =  [i['volume'] for i in listaItens]
    
    pendentes = []
    naoPendentes = []
    for veiculo in listaVeiculos:
        peso = veiculo['peso']
        volume = veiculo['volume']
        placa = veiculo ['placa']
        listaDicionarios = listaItens.copy()

        valoresPesos = knapSack(peso, pesosPeso, listaDicionarios, intMercadoria, 'peso')
        setta_1(valoresPesos, listaDicionarios, 'peso')

        valoreVolumes = knapSack(volume, pesosVolume, listaDicionarios, intMercadoria, 'volume')
        setta_1(valoreVolumes, listaDicionarios, 'volume')
        juntos = intersecao(valoresPesos, valoreVolumes, pendentes, naoPendentes)
        # resultado = retornaDicionario(juntos, listaItensCopia)
        imprimeValores(peso, volume, listaItensCopia, juntos, placa )
    imprimePendentes(listaItensCopia, pendentes)
        
def imprimeValores(capacidadePeso, capacidadeVolume,listaCopia, lista, placa):
    somaPeso = 0
    somaVolume = 0
    somaValor = 0
    for indice in lista:
        somaPeso += listaCopia[indice]['peso']
        somaVolume += listaCopia[indice]['volume']
        somaValor += listaCopia[indice]['valor']
  
    arquivoSaida.write(f'[{placa}]R${somaValor:.2f},{somaPeso}KG({porcentagem(capacidadePeso, somaPeso)}%),{somaVolume}L({porcentagem(capacidadeVolume, somaVolume)}%)\n')
    for indice in lista:
        arquivoSaida.write(f'{listaCopia[indice]["SuaChave"]}\n')
    

def imprimePendentes(listaCopia, pendentes):
    somaPeso = 0
    somaVolume = 0
    somaValor = 0
    for indice in pendentes:
        somaPeso += listaCopia[indice]['peso']
        somaVolume += listaCopia[indice]['volume']
        somaValor += listaCopia[indice]['valor']
    arquivoSaida.write(f'[PENDENTE]R${somaValor:.2f},{somaPeso}KG,{somaVolume}L\n')
    for indice in pendentes:
        arquivoSaida.write(f'{listaCopia[indice]["SuaChave"]}\n')
    


verificaPesos(listaVeiculos, listaItens, listaItensCopia)
# print(f'{porcentagem(50, 49)}')




fim = time.time()

# print(sorted([{"a": 3, "b": 3}, {"a": 4, "b": 1},  {"a": 4, "b": 4}], key= lambda item: item['b'], reverse=True))
print('tempo', fim - inicio)

