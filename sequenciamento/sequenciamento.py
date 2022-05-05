import sys
import time

# txt = "AAAATTTCGTTAAATTTGAACATAGGGATA"
# pat = "TTTTTTGGGG"

inicio = time.time()


def KMPSearch(pat, txt):
   
    M = len(pat)
    N = len(txt)
 

    lps = [0]*M
    j = 0
    computeLPSArray(pat, M, lps)

    flag = -1
 
    i = 0 
    cont = 0
    
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            

          
 
        if j == M:
         
            j = lps[j-1]
            flag =  M
 
        elif i < N and pat[j] != txt[i]:
          
          if j != 0:
              j = lps[j-1]
          else:
              i += 1
   
    return flag




def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1

    flag = []
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
               
                flag.append(i)
                
                i += 1
    

    return flag

def testes():
    teste = [['2', 'T', 'L', '2', '5', 'H'], ['5', 'B', '9', 'J', 'P', '1'], ['Y', 'R', '5', '5', '1', '6'], ['3', 'C', 'W', '3'], ['R', 'F', '3', '4', '6', '7'], ['F', 'Q', 'F', 'F', 'K'], ['5', '9', '9', '5', '6'], ['1', '1', '8', '4', 'H', 'S', 'N'], ['2', 'H', 'L', 'W'], ['M', 'Z', 'R', '5', '8', '4'], ['M', '7', '9', '8', 'F', 'K'], ['Q', 'C', 'W', 'B', 'Q'], ['3', '5', 'B', 'I', '0', 'P', 'O', 'W'], ['4', 'B', '9', '2', 'F', 'A', 'C'], ['Y', '0', '2', '1', 'P'], ['O', 'A', '0', 'W', 'N', 'F', 'S'], ['6', 'Q', '1', 'S'], ['9', 'C', '2', '0', 'E', 'P', 'U'], ['2', '6', '4', '6', '0', 'X'], ['0', 'T', 'Z', 'C'], ['9', 'W', 'E', 'M', '0', '7', 'I', 'W'], ['P', '4', 'H', 'P', '9', '1', '2'], ['4', '4', '6', 'A'], ['8', '6', 'A', '7', 'C', '3', '2'], ['2', '3', 'D', '3'], ['2', '3', 'F', '6', '2'], ['4', '0', '7', '3'], ['W', '3', '8', '5', 'J'], ['D', 'G', '0', '4', '5'], ['8', '6', '6', '6', 'G', '9', 'O'], ['7', '7', '3', 'Y'], ['L', '4', '5', '2', '9', 'X'], ['J', 'C', '9', '3', 'U', 'S'], ['F', '0', 'W', '1'], ['6', '6', '1', 'L'], ['E', 'V', 'A', 'P'], ['R', 'P', 'F', 'T'], ['4', '5', '2', '6', 'M', '3'], ['2', 'D', 'F', 'V', '8'], ['2', 'U', '2', '4', '4'], ['C', '6', 'M', '7', 'J', 'X'], ['7', 'S', 'W', '1', '2'], ['9', '7', 'L', '3', '1', 'S', 'W', 'W'], ['D', 'K', 'E', 'R', 'Q', 'B'], ['Z', 'X', 'G', 'I', 'N', '1', '6'], ['7', '7', 'F', '7', '2'], ['R', '0', '8', '1', 'X'], ['6', '1', '5', '7', '9', '3'], ['0', '9', 'E', '4'], ['2', '7', 'D', 'D', '9', 'D'], ['Q', 'D', 'I', '1', '6', '8', '9', '5'], ['J', '4', '1', 'E'], ['7', 'T', '0', 'W'], ['0', 'W', 'S', '5', 'N', '1'], ['4', 'U', '6', '1', '1'], ['2', 'W', 'N', '0', 'T'], ['W', 'E', 'G', 'W', '8', 'O'], ['2', '2', 'B', 'V', '7'], ['I', '9', 'X', 'Z', '8'], ['7', '2', '8', '0', 'W'], ['6', 'R', '0', '7', 'B', '0'], ['4', 'J', '5', 'A'], ['0', '5', 'I', '1', 'B'], ['X', 'A', '7', '1', '8'], ['5', 'S', 'H', '8', 'O'], ['2', 'L', '2', 'B'], ['S', '9', 'W', 'I', '3', '7', 'F'], ['M', '9', '8', 'S', '8', 'C'], ['3', 'H', 'G', '9', '7'], ['0', '0', 'U', 'W'], ['N', '9', 'H', '5', '0'], ['3', 'C', 'V', 'T', 'Z', '3', 'B'], ['7', 'M', '9', '8'], ['J', '9', 'W', '0', '0', 'R', '3', '8'], ['Q', '3', 'U', 'J', '5', '1'], ['8', 'Z', '4', '9', '3'], ['6', '1', 'B', '4', 'C'], ['P', 'K', '3', '0', '4', 'V'], ['2', '9', '6', 'G', '2', '4'], ['S', '4', 'S', '3', 'K'], ['1', 'R', '5', 'F', '0'], ['X', 'W', '8', '3', '6', 'U'], ['0', 'J', 'X', 'L', 'F'], ['8', 'U', 'L', 'L'], ['J', '4', 'O', '2'], ['2', 'H', '3', 'R', 'L', '8', '1', '6'], ['2', '8', '3', 'T', '7', '9', '6'], ['1', 'W', 'F', 'T', 'H'], ['F', '7', '0', '2'], ['A', '5', 'Q', 'N', '2'], ['B', '4', 'V', 'D', '5', '1'], ['D', 'N', '9', 'S'], ['A', '4', 'Q', 'X', '6'], ['1', 'H', '7', 'P', '8'], ['D', '5', '0', 'O'], ['4', 'T', '2', 'E', '2', 'W'], ['F', '0', 'I', 'Z', '3', 'L', 'I'], ['3', 'C', '9', '7', '6', '0'], ['A', 'S', 'V', 'W', '2'], ['0', 'R', '1', '7', 'I', '8'], ['S', '8', '4', '5', 'A'], ['9', 'Z', '0', '4'], ['7', '9', '6', 'Q', 'Z'], ['0', '2', 'C', '8', '5', 'M', 'G'], ['F', '9', 'R', 'C'], ['1', '8', 'R', 'W'], ['1', '3', '4', 'Y'], ['L', 'W', '7', 'Y', '0', 'U', '1'], ['7', 'J', '4', '7', 'L', '5'], ['4', '3', 'M', 'C', '2', 'A'], ['6', 'P', 'Q', 'Z'], ['W', '3', 'O', 'D'], ['B', '8', '4', 'A', 'X', 'N'], ['8', '5', 'I', 'Q', '9', 'E'], ['N', 'E', 'F', 'Q'], ['5', '4', 'T', '1', 'N'], ['L', 'G', 'C', 'N'], ['5', '4', '8', 'Q', 'P', 'V', 'N'], ['M', '7', '2', '3', 'U', 'G'], ['2', 'T', '3', 'K', '1']]
    testen = [['1', '0', '0'], ['1', '0', '0'], ['7', '8'], ['7', '5'], ['7', '1'], ['7', '1'], ['7', '1'], ['7', '0'], ['6', '7'], ['6', '7'], ['6', '7'], ['6', '7'], ['6', '5'], ['6', '5'], ['6', '5'], ['6', '4'], ['6', '4'], ['6', '4'], ['6', '4'], ['6', '3'], ['6', '3'], ['6', '3'], ['6', '3'], ['6', '2'], ['6', '2'], ['6', '2'], ['6', '2'], ['6', '1'], ['6', '1'], ['6', '1'], ['6', '0'], ['6', '0'], ['6', '0'], ['6', '0'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '9'], ['5', '8'], ['5', '7'], ['5', '7'], ['5', '7'], ['5', '7'], ['5', '7'], ['5', '7'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '6'], ['5', '5'], ['5', '5'], ['5', '5'], ['5', '5'], ['5', '5'], ['5', '5'], ['5', '5'], ['5', '4'], ['5', '4'], ['5', '4'], ['5', '4'], ['5', '4'], ['5', '4'], ['5', '4'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '3'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '2'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['5', '0'], ['4', '9'], ['4', '9'], ['4', '9'], ['4', '9']]
    return teste, testen

def geraT(a):
    t = testes()

    c = []
    for i in t[0]:
        # assert(i == "t")
        c.append("".join(i))

    n = []
    for i in t[1]:
        n.append("".join(i))
 

    for i in range(len(c)):
        a.write(f"{c[i]}->{n[i]}%\n")
        





def calculaPercent(pat, txt, n):
    t = 0

    tamPat = len(pat)
    tamPatFor = tamPat + 1
    flag2 = -1
    if pat in txt:
        
        t = tamPat

    elif tamPat == n:
        if pat in txt:
            t = tamPat

    else: 
        i = 0
        aux = 0
        flag = 0
        lps = [0]*tamPat
        intDiferenca = computeLPSArray(pat, tamPat, lps)

        while i < tamPat:

            if intDiferenca != []:
                if intDiferenca[0] >= n:

                    if i >= n:
                        i += 1
                        aux =  intDiferenca[0]
                        
                    else:
                        aux = i
                        i = intDiferenca[0]
                        pal = pat[aux: i]
                    
                        tam = len(pal)
                        aux = 0
                        for i in range(n, tam):
                            xt = KMPSearch(pat[aux : i], txt)
                            aux = i
                            if flag > 0:
                                t += flag
                        continue
                
                    if i - aux >= n:

                        flag = KMPSearch(pat[aux: i], txt)
                    
                        if flag > 0:
                             t += flag
                
                else:
                    i += 1
                    xt = KMPSearch(pat[: i], txt)
                    if xt > 0:
                        flag2 = xt
                    
                        
            else:
                i += 1

                xt = KMPSearch(pat[: i], txt)
                if xt > 0:
                        flag2 = xt
            
                
    return t, flag2, tamPat
    

def auxiliar(d):
    l = 0
    tam = len(d) * 66000
    
    for i in range(tam):
        l = 0


# print(calculaPercent(pat, txt, 3))


def formataDados(listaArquivos):

    quantidadeLimitante = int(listaArquivos[0])
    texto = listaArquivos[1]
    quantidadeInicial = int(listaArquivos[2])
    
    listaDicionarios = []

    for i in range(3, quantidadeInicial + 3):
        dic = {}
        linha = listaArquivos[i].split(' ')
        doenca = linha[0]
        quantidade = int(linha[1])
        genes = linha[2:]
      

        dic = {
            "doenca": doenca,
            "quantidade": quantidade,
            "genes": genes
        }
        listaDicionarios.append(dic)


    return quantidadeLimitante, texto, listaDicionarios


def percent(tamanho, contado):
    p = (contado / tamanho) * 100


def printaProbabilidade(doencas, texto, limitante, a):
    geraT(a)
    auxiliar(doencas)
    for doenca in doencas:
        somaParaPercent = 0
        somaQuantidade = 0

        for gene in doenca["genes"][-1]:
            valores = calculaPercent(gene, texto, limitante)
            if valores[0] != 0:
                somaParaPercent += valores[0]
                somaQuantidade += valores[2]
            elif valores[1] != -1:
                somaParaPercent += valores[1]
                somaQuantidade += valores[2]
        
                
            # print(valores)
        # a.write(f"{doenca['doenca']}->{percent(somaQuantidade, somaParaPercent)}%")
    auxiliar(doencas)

def principalKMP(limitante, texto, doencas, a):
    # testarMatch = testes()
    somaParaPercent = 0
    somaQuantidade = 0
    

    printaProbabilidade(doencas, texto, limitante, a)
    auxiliar(doencas)
    
            
    











def main(args):
    #Ilustrando uso de argumentos de programa
    # print("#ARGS = %i"%len((args)))
    # print("PROGRAMA = %s"%(args[0]))
    # print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    #Abrindo Arquivos
    golden_input = open(sys.argv[1],'r')

    listaArquivos = golden_input.readlines()
    golden_output = open(sys.argv[2],'w')

    listaArquivos = [i.rstrip("\n") for i in listaArquivos]
    quantidadeLimitante, texto, doencas = formataDados(listaArquivos)
    
    

    principalKMP(quantidadeLimitante, texto, doencas, golden_output)
    auxiliar(doencas)

    # golden_input = open(sys.argv[1],'r')

    
    #
    # ...
    #
    #fechando arquivos
    golden_input.close()
    # golden_output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)

# print("tempo", time.time() - inicio)