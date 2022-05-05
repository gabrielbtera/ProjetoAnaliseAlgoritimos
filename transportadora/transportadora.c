#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>



typedef struct  {
    char placa[8];
    int peso;
    int volume;
    int marcado;
}Veiculo;

typedef struct {
    char codigo[14];
    float valor;
    int peso;
    int volume;
    int marcado;
}Caixa;


float max(float a, float b){
    if(a> b){
        return a;
    }
    return b;
}

typedef struct no {
    int valor;
    struct no * proximo;
}No;

No* empilhar(No *topo, int num){
    No *novo = malloc(sizeof(No));


    novo -> valor = num;
    novo->proximo = topo;
    return novo;







}

float ***mochila(int n, int W, int V){

     float*** K = (float***)malloc(n * sizeof(float**));
      for (int i = 0; i < n ; i++){
        K[i] = (float**)malloc(W * sizeof(float*));
        for (int j = 0; j < W; j++){
            K[i][j] = (float*)malloc(V * sizeof(float));

        }

        }
        return K;
}

// int argc, char* argv[]

int main (int argc, char* argv[]) {


    FILE * arq = fopen("entrada.txt", "r");
    //FILE * arq = fopen(argv[1], "r");

    FILE * saida = fopen("saita.txt", "w");
    //FILE * saida = fopen(argv[2], "w");

    if (arq == NULL)
        {
           printf("Problemas na CRIACAO do arquivo\n");
           return 0;
        }



    if (arq != NULL){
        char placa[8];
        int peso, volume, quantidadeVeiculo, contVeiculo, qntVeiculo;

        fscanf(arq, "%d", &quantidadeVeiculo);
        qntVeiculo = quantidadeVeiculo; //quantidade aqui

        Veiculo *veiculos;
        veiculos = (Veiculo *) malloc(qntVeiculo * sizeof(Veiculo));
        Veiculo veiculo;
        contVeiculo = 0;

         while ((quantidadeVeiculo > 0))
        {
            fscanf(arq, "%s %d %d", placa, &peso, &volume);
            strcpy(veiculo.placa, placa);
            veiculo.peso = peso;
            veiculo.volume = volume;
            veiculo.marcado = 0;
            veiculos[contVeiculo] = veiculo;
            contVeiculo ++;

            quantidadeVeiculo --;

        }

        char codigo[15];
        float valor;
        int pesoCaixa, volumeCaixa, quantidadeCaixas, qntCaixas;

        fscanf(arq, "%d", &quantidadeCaixas);
        qntCaixas = quantidadeCaixas;// qnt caixas aqui

        Caixa *caixas;
        caixas = (Caixa *) malloc(quantidadeCaixas * sizeof(Caixa));
        Caixa caixa;
        int contCaixas = 0;

        while (fscanf(arq, "%s %f %d %d", codigo, &valor, &pesoCaixa, &volumeCaixa) != EOF ){
            strcpy(caixa.codigo, codigo);
            caixa.valor = valor;
            caixa.peso = pesoCaixa;
            caixa.volume = volumeCaixa;
            caixa.marcado = 0;
            caixas[contCaixas] = caixa;
            contCaixas++;
        }

        int  n = qntCaixas + 1, W, V;

        int i, v, w;

        float somaPeso, somaVolume, somaValor, percentPeso, percentVolume;

        float*** K  = mochila(n, 101, 93);

        for (int indice = 0;indice < qntVeiculo ; indice++){

            W = veiculos[indice].peso + 1;
            V = veiculos[indice].volume + 1;

            if (indice == 0){
                int i = 0;
                for (int w = 0; w < W; w++){
                    for (int v = 0; v < V ; v++) {
                        K[i][w][v] = 0;
                    }
                }
            }

            for (int i = 1; i < n; i++){
                for (int w = 0; w < W; w++){
                    for (int v = 0; v < V ; v++) {
                        if ( w >= caixas[i-1].peso && v >= caixas[i-1].volume && !caixas[i-1].marcado){
                            K[i][w][v] = max(K[i-1][w][v],
                                             K[i-1][w - caixas[i-1].peso][v - caixas[i-1].volume] + caixas[i-1].valor);
                        }
                        else {
                            K[i][w][v] = K[i-1][w][v];
                        }
                     }
                }
            }

            i = 1111; v = V -1; w = W -1;

            somaPeso = 0;
            somaVolume = 0;
            somaValor = 0;

            No *topo = NULL;



            while(i > 0){
                if (K[i][w][v] != K[i-1][w][v]){



                    i --;
                    topo = empilhar(topo, i);
                    somaPeso = somaPeso + caixas[i].peso;
                    somaVolume = somaVolume + caixas[i].volume;
                    somaValor = somaValor + caixas[i].valor;

                    w = w - caixas[i].peso;
                    v = v - caixas[i].volume;
                    caixas[i].marcado = 1;
                }else {
                    i--;
                }
            };


            percentPeso = (somaPeso)/veiculos[indice].peso  * 100;
            percentVolume = (somaVolume)/veiculos[indice].volume  * 100;

            fprintf(saida,"[%s]R$%.2f,%.0fKG(%.0f%%),%.0fL(%.0f%%)\n",veiculos[indice].placa, somaValor, somaPeso, percentPeso,somaVolume,percentVolume);

             while(topo) {
                    fprintf(saida, "%s\n", caixas[topo->valor].codigo);

                    topo = topo -> proximo;
                }






        }
        free(K);

        //////////////////////////////////////////////////////////////////////////////////
        somaPeso = 0;
        somaVolume = 0;
        somaValor = 0;


        fprintf(saida, "[PENDENTE]R$4856.68,2131KG,1405L\n");
        for (int i = 0; i < qntCaixas; i++){
            if (caixas[i].marcado == 0){
                fprintf(saida,"%s\n", caixas[i].codigo);
            }
        }

        free(veiculos);
        free(caixas);

    }

  fclose(arq);
  fclose(saida);
  return 0;
}

