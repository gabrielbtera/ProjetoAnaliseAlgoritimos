#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdint>

using namespace std;

typedef struct{
	string nomeDoenca;
	uint32_t contador;
} seqDoenca;


uint32_t contadorAcertos(char *dnaPessoa, char *cadeiaDoenca, uint32_t inicioDNA, uint32_t inicioCadeia, uint32_t tamanhoCadeia){

	uint32_t t = tamanhoCadeia, iteracao, acerto = 0;

	for(iteracao = 0; iteracao < t ; iteracao ++ )
		if(dnaPessoa[inicioDNA + iteracao] != cadeiaDoenca[inicioCadeia + iteracao])
			return acerto;
		else acerto++;
	return acerto;
}
uint32_t nround(float n){return n + 0.5;}
seqDoenca **countingSort(seqDoenca**, uint32_t, uint32_t);


int main(int argc, char *argv[]){
	ifstream entrada("entrada2.txt");
	ofstream saida("saida2.txt");

	uint32_t tamanhoMaxCadeia = 10000, tamanhoMaxDNA = 101;

	char cadeia[tamanhoMaxCadeia], *dnaPessoa;

	string preload;


	uint32_t quantidade, quantidadeMinima;

	entrada >> quantidadeMinima >> preload >> quantidade;
    dnaPessoa = (char*)preload.c_str();

    uint32_t iguais, acertos;

	seqDoenca **todasDoencas = new seqDoenca*[quantidade];

    uint32_t tamanhoDNAPessoa, tamanhoCadeia, inicioDNA, inicioCadeia, quantidadeCada;
	tamanhoDNAPessoa = strlen(dnaPessoa);

	uint32_t contaAcertos, contaGenes;

	for(uint32_t i = 0; i < quantidade; i++){

		seqDoenca *genesDoenca = new seqDoenca;
		entrada >> genesDoenca->nomeDoenca >> quantidadeCada;
		contaGenes = 0;

		for(uint32_t j = 0; j < quantidadeCada; ++j){
            entrada >> cadeia;

            iguais = 0;

            inicioDNA = 0; inicioCadeia = 0;
			tamanhoCadeia = strlen(cadeia);
			while(inicioDNA < tamanhoDNAPessoa && inicioCadeia < tamanhoCadeia)
            {
				contaAcertos = contadorAcertos(dnaPessoa, cadeia, inicioDNA, inicioCadeia, tamanhoCadeia);

				if(contaAcertos >= quantidadeMinima){
					iguais += contaAcertos;
					inicioDNA += contaAcertos;
					inicioCadeia += contaAcertos;
				}else inicioDNA++;

			}
			acertos = (100.00*iguais/tamanhoCadeia) + 0.5;
			if(acertos >= 90) contaGenes++;
		}
		genesDoenca->contador = (100.00*contaGenes/quantidadeCada) + 0.5;
		todasDoencas[i] = genesDoenca;
	}
	todasDoencas = countingSort(todasDoencas, quantidade, tamanhoMaxDNA);

	for(uint32_t i = 0; i < quantidade; ++i)
		saida << todasDoencas[i]->nomeDoenca << "->" << todasDoencas[i]->contador << "%\n";



    entrada.close();
	saida.close();
	return 0;
}


seqDoenca **countingSort(seqDoenca **todasDoencas, uint32_t n , uint32_t tamanhoMaxDNA){
	uint32_t i;
	uint32_t cadeia[tamanhoMaxDNA];
	for(i = 0; i < tamanhoMaxDNA; ++i)
		cadeia[i] = 0;
	for(i = 0; i < n; ++i){
		cadeia[todasDoencas[i]->contador]++;
	}
	uint32_t anterior = 0;
	for(i = tamanhoMaxDNA; i > 0; --i){
		cadeia[i-1] += anterior;
		anterior = cadeia[i-1];
	}
	seqDoenca **u =  new seqDoenca*[n];
	for(i = n;	i > 0; --i)
		u[--cadeia[todasDoencas[i-1]->contador]] = todasDoencas[i-1];
	return u;
}



