import sys
import time

inicio = time.time()

def contMatchs(dna, cadeia, tamanhoCadeia, tamanhoDNA,InicioDna,  inicioCadeia ):
    cont = 0
    i = 0
    t = tamanhoCadeia
    while i < t and i + inicioCadeia < tamanhoCadeia and i + InicioDna < tamanhoDNA:
        
        if dna[InicioDna + i] != cadeia[inicioCadeia + i]:
            return cont
        else:
            cont += 1
        i += 1
    
    return cont

def percent(tamanho, contado):
    return (contado / tamanho) * 100


def calculaMatchs(minimo, dna, doencas):
    tamanhoDNA = len(dna)
    for doenca in doencas:
        quantidade = doenca['quantidade']
        genes = doenca['genes']
        geneAdd = 0
        for cadeia in genes:
            tamanhoCadeia = len(cadeia)
            iguais = 0
            inicioDna = 0
            inicioCadeia = 0
            while inicioDna < tamanhoDNA and inicioCadeia < tamanhoCadeia:
                contador = contMatchs(dna, cadeia, tamanhoCadeia, tamanhoDNA, inicioDna, inicioCadeia)

                if tamanhoCadeia == contador:
                    inicioCadeia = tamanhoCadeia

                if(contador >= minimo):
                    iguais += contador
                    inicioDna += contador
                    inicioCadeia += contador
                else:
                    inicioDna += 1

            acertos = percent(tamanhoCadeia, iguais)
            if acertos >= 90:
                geneAdd += 1

        doenca['percentual'] = round(percent(quantidade, geneAdd))
    return sorted(doencas, key=lambda qnt: qnt["percentual"], reverse=True)


def printaSaida(arquivo, ordenados):
    for seq in ordenados:
        arquivo.write(f'{seq["doenca"]}->{seq["percentual"]}%\n')

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
            "genes": genes,
            "percentual": 0
        }
        listaDicionarios.append(dic)
    return quantidadeLimitante, texto, listaDicionarios
    

def main(args):
    #Ilustrando uso de argumentos de programa
    # print("#ARGS = %i"%len((args)))
    # print("PROGRAMA = %s"%(args[0]))
    # print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))
    #Abrindo Arquivos
    golden_input = open("entrada.txt", "r")

    listaArquivos = golden_input.readlines()
    golden_output = open("saida.txt",'w')

    listaArquivos = [i.rstrip("\n") for i in listaArquivos]
    quantidadeLimitante, dna, doencas = formataDados(listaArquivos)

    
    printaSaida(golden_output, calculaMatchs(quantidadeLimitante,dna,  doencas))
    
    # golden_input = open(sys.argv[1],'r')
    
    golden_input.close()
    golden_output.close()


if __name__ == '__main__':
    main(sys.argv)

print("tempo", time.time() - inicio)
