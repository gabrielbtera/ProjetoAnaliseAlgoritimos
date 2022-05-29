#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdint>

using namespace std;


uint32_t contadorAcertos(char *dnaPessoa, char *cadeiaDoenca, uint32_t inicioDNA, uint32_t inicioCadeia, uint32_t tamanhoCadeia){

	uint32_t t = tamanhoCadeia, iteracao, acerto = 0;

	for(iteracao = 0; iteracao < t ; iteracao ++ )
		if(dnaPessoa[inicioDNA + iteracao] != cadeiaDoenca[inicioCadeia + iteracao])
			return acerto;
		else acerto++;
	return acerto;
}

typedef struct{
	string nomeDoenca;
	uint32_t contador;
} seqDoenca;



void ordenacao(seqDoenca **todasDoencas,ofstream& saida,  uint32_t quantidade , uint32_t tamanhoMaxDNA){

	uint32_t cadeia[tamanhoMaxDNA];
	uint32_t i;
	for(i = 0; i < tamanhoMaxDNA; ++i)
		cadeia[i] = 0;

	for(i = 0; i < quantidade; ++i){
		cadeia[todasDoencas[i]->contador]++;
	}

	uint32_t anterior = 0;
	for(i = tamanhoMaxDNA; i > 0; --i){
		cadeia[i-1] += anterior;
		anterior = cadeia[i-1];
	}
	seqDoenca **u =  new seqDoenca*[quantidade];
	for(i = quantidade;	i > 0; --i){
		u[--cadeia[todasDoencas[i-1]->contador]] = todasDoencas[i-1];




	}

	for(uint32_t i = 0; i < quantidade; i++)
		saida << u[i]->nomeDoenca << "->" << u[i]->contador << "%\n";
}

float arredondar(uint32_t conta, uint32_t quantidade){
    return (100.00*conta/quantidade) + 0.5;

}

int main(int argc, char *argv[]){



	uint32_t tamanhoMaxCadeia = 10000, tamanhoMaxDNA = 101;
	char cadeia[tamanhoMaxCadeia], *dnaPessoa;
	ifstream entrada("entrada2.txt");

	uint32_t quantidade, quantidadeMinima;
    string preload;
	entrada >> quantidadeMinima >> preload >> quantidade;

  uint32_t tamanhoDNAPessoa, tamanhoCadeia, inicioDNA, inicioCadeia, quantidadeCada;


	tamanhoDNAPessoa = strlen((char*)preload.c_str());


	uint32_t contaAcertos, contaGenes;
	uint32_t iguais;

	seqDoenca **todasDoencas = new seqDoenca*[quantidade];
	dnaPessoa = (char*)preload.c_str();
	for(uint32_t i = 0; i < quantidade; i++){

		seqDoenca *genesDoenca = new seqDoenca;
		entrada >> genesDoenca->nomeDoenca >> quantidadeCada;
		contaGenes = 0;

		for(uint32_t y = 0; y < quantidadeCada; y++){
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

			if(arredondar(iguais, tamanhoCadeia) >= 90){
                contaGenes++;
			}
		}
		genesDoenca->contador = arredondar(contaGenes, quantidadeCada);
		todasDoencas[i] = genesDoenca;
	}
	ofstream saida("saida2.txt");
	ordenacao(todasDoencas,saida, quantidade, tamanhoMaxDNA);

	entrada.close();
	saida.close();
	return 0;
}








