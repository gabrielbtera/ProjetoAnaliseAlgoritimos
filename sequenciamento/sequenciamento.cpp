#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdint>

using namespace std;

typedef struct{
	string codigo;
	uint32_t acerto;
} sequencia;

uint32_t nround(float n){return n + 0.5;}
uint32_t count_matchs(char*, char*, uint32_t, uint32_t);
sequencia **countingsort(sequencia**, uint32_t, uint32_t);

int main(int argc, char *argv[]){
	ifstream input(argv[1]);
	ofstream output(argv[2]);
  
	uint32_t min, cases, inita, initb, matchs, acertos, genes, n;
	char buffer[10000], *dna;
	string temp;
	
	input >> min >> temp >> cases;
	dna = (char*)temp.c_str();
	
	sequencia **sequencias = new sequencia*[cases];

	for(uint32_t i = 0; i < cases; ++i){
		sequencia *a = new sequencia;
		input >> a->codigo >> n;
		genes = 0;
		for(uint32_t j = 0; j < n; ++j){
			inita = 0;
			initb = 0;
			matchs = 0;
			input >> buffer;
			while(inita < (uint32_t)strlen(dna) && initb < (uint32_t)strlen(buffer)){
				uint32_t count = count_matchs(dna, buffer, inita, initb);
				if(count >= min){
					matchs += count;
					inita += count;
					initb += count;
				}
				else inita++;
			}
			acertos = nround(100.00*matchs/strlen(buffer));
			if(acertos >= 90) genes++;
		}
		a->acerto = nround(100.00*genes/n);
		sequencias[i] = a;
	}
	
	sequencias = countingsort(sequencias, cases, 101);
	input.close();
	for(uint32_t i = 0; i < cases; ++i)
		output << sequencias[i]->codigo << "->" << sequencias[i]->acerto << "%\n";
	output.close();
	return 0;
}

uint32_t count_matchs(char *xs, char *ys, uint32_t initxs, uint32_t initys){
	uint32_t count = 0;
	uint32_t t = strlen(ys);
	for(uint32_t i = 0; i < t && xs[i] != '\0'; ++i)
		if(xs[initxs+i] != ys[initys+i])
			return count;
		else count++;
	return count;
}

sequencia **countingsort(sequencia **v, uint32_t n, uint32_t k){
	uint32_t i;
	uint32_t w[k];
	for(i = 0; i < k; ++i)
		w[i] = 0;
	for(i = 0; i < n; ++i){
		++w[v[i]->acerto];
	}
	uint32_t ant = 0;
	for(i = k; i > 0; --i){
		w[i-1] += ant;
		ant = w[i-1];
	}
	sequencia **u =  new sequencia*[n];
	for(i = n;	i > 0; --i)
		u[--w[v[i-1]->acerto]] = v[i-1];
	return u;
}
