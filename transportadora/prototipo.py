from copy import deepcopy
from math import ceil
from re import A
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
            'SuaChave':quebrado[0],
            'set': 0}

    listaItens.append(dic)

listaItens = sorted(listaItens, key= lambda item: item['valor'], reverse=True)

#listaItensCopia = deepcopy(listaItens)

print(listaItens)

def minhaMax (a, b):
    if a > b:
        return a
    return b

def knapSack(W,V , val, n, opcao):

    
    K = [[[0] * (V + 1)]* (W + 1) for _ in range(n + 1)]
    # print(K[5][50][100])


    for i in range(1, n + 1 ):
        
        
        for w in range(W + 1):
            
            for v in range (V + 1):
               
                
                if w >= val[i-1]['peso'] and  v >= val[i-1]['volume']  and not val[i-1]["set"]:
                    K[i][w][v] = max(K[i-1][w][v], 
                    K[i-1][w - val[i-1]['peso']][v - val[i-1]['volume']] + val[i-1]['valor'])
                    arquivoSaida.write(f"{K[i][w][v]}\nmeu {i} p{val[i-1]['peso']} pp {w} vv{v-val[i-1]['volume']} v{v}\n cond {w >= val[i-1]['peso'] and  v >= val[i-1]['volume']}\n")
                    
                else:
                    K[i][w][v] = K[i-1][w][v]
                    arquivoSaida.write(f"\nMeu iiii {i-1}\n")


    i = n - 1
    w = W
    v = V
    lista = []

    print(K[n][W][V])

    while i >= 0:

        if  K[i][w][v] != K[i-1][w][v]:
            
           
            
            lista.append(i)
            w = w - val[i]['peso']
            v = v - val[i]['volume']
            i -= 1
            
            

        else:
            print("aqui")
            i-= 1
        
   
    print(lista)
  
    return lista
  

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


    for veiculo in listaVeiculos:
        peso = veiculo['peso']
        volume = veiculo['volume']
        placa = veiculo ['placa']
        # listaDicionarios = listaItens.copy()


        numeros = knapSack(peso, volume, listaItens, intMercadoria, "")

        



       
        # resultado = retornaDicionario(juntos, listaItensCopia)
        # imprimeValores(peso, volume, listaItensCopia, juntos, placa )
    # imprimePendentes(listaItensCopia, pendentes)
        
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

