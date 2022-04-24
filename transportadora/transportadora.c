#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


typedef struct  {
    char placa[8];
    uint32_t peso;
    uint32_t volume;
}Veiculo;

typedef struct {
    char codigo[14];
    double valor;
    uint32_t peso;
    uint32_t volume;
}Caixa;


void ImprimePessoa(Veiculo veiculo) // declara o parâmetro como uma struct
{
  printf("aqui %s %d %d\n",veiculo.placa, veiculo.peso, veiculo.volume);
}


int main (void) {


    FILE * arq = fopen("entrada.txt", "r");



    if (arq != NULL){
        char placa[8];
        uint32_t peso, volume, quantidadeVeiculo, contVeiculo, qntVeiculo;

        fscanf(arq, "%d", &quantidadeVeiculo);
        qntVeiculo = quantidadeVeiculo;
        Veiculo veiculos[quantidadeVeiculo];
        Veiculo veiculo;
        contVeiculo = 0;

         while ((quantidadeVeiculo > 0))
        {
            fscanf(arq, "%s %d %d", placa, &peso, &volume);
            strcpy(veiculo.placa, placa);
            veiculo.peso = peso;
            veiculo.volume = volume;
            veiculos[contVeiculo] = veiculo;



            quantidadeVeiculo = quantidadeVeiculo - 1;

        }
        int i;
        for (i = 0; i < qntVeiculo; i = i + 1){
            ImprimePessoa(veiculos[i]);
            printf("\n%d\n", i);
        }



        char codigo[15];
        float valor;
        uint32_t pesoCaixa, volumeCaixa, quantidadeCaixas, qntCaixas;
        fscanf(arq, "%d", &quantidadeCaixas);
        qntCaixas = quantidadeCaixas;
        Caixa caixas[quantidadeCaixas];
        Caixa caixa;
        int contCaixas = 0;

        while (fscanf(arq, "%s %f %d %d", codigo, &valor, &pesoCaixa, &volumeCaixa) != EOF && quantidadeCaixas > 0){

            printf("%s %.2f %d %d\n", codigo, valor, pesoCaixa, volumeCaixa);
            strcpy(caixa.codigo, codigo);
            caixa.valor = valor;
            caixa.peso = pesoCaixa;
            caixa.volume = volumeCaixa;

            caixas[contVeiculo] = caixa;
            quantidadeCaixas = quantidadeCaixas - 1;
            contVeiculo = contVeiculo + 1;
        }






    }

  fclose(arq);
  return 0;
}
