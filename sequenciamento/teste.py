

def contMatchs(dna, cadeia, tamanhoCadeia, tamanhoDNA,InicioDna,  inicioCadeia ):
    cont = 0
    i = 0
    j = 0
    t = tamanhoCadeia

    while i < t and i + inicioCadeia < tamanhoCadeia and i + InicioDna < tamanhoDNA:
        
        if dna[InicioDna + i] != cadeia[inicioCadeia + i]:
            return cont
        else:
            cont += 1
        
        i += 1
        j += 1
    
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
        

   








