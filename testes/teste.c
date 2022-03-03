#include <stdio.h>
#include <conio.h>
#include <stdint.h>
#include <string.h>

#include <time.h>


typedef struct 
{
  int numeroConteiners;
  char codigo[12];
  char CNPJ[19];
  int32_t Peso;
}Conteiner;




typedef struct 
{
  Conteiner conteiners[10]

}DadosConteiners;




void abrirArquivo(){
  FILE *file;

  
  char codigo[12];
  char CNPJ[19];
  int32_t peso;

  printf( "\nAbrir arquivo \n");
  

  file = fopen("teste2.txt", "r");
  if (file == NULL){
    printf("Arquivo não encontrado");
  }else{
    printf("Arquivo aberto.\n");
  }

  Conteiner conteiner;
  DadosConteiners dadosConteiners;

  int32_t numeroConteiners = 0;
  fscanf(file, "%d[^\n]", &numeroConteiners);

  int32_t indice = 0;

  while (fscanf(file, "%s %s %d[^\n]\n",&codigo,  &CNPJ,   &peso) != EOF){
    numeroConteiners--;
    
    if (!numeroConteiners){
      fscanf(file, "%d[^\n]", &numeroConteiners);
    }
    printf("Codigo: %s\nCNPJ: %s\nPeso:%d\n", codigo,CNPJ, peso);

    strcpy(conteiner.codigo, codigo);
    strcpy(conteiner.CNPJ, CNPJ);
    conteiner.Peso = peso;
    dadosConteiners.conteiners[indice] = conteiner;

    printf("----------------------%s-------------------------\n");
    
    

  }
  

  
 
  fclose(file);
  

}


int main(void)
{
  clock_t t;
  printf("Tempo de execucao: %lf", ((double)t)/((CLOCKS_PER_SEC
  )));
  t = clock();
  abrirArquivo(1000000);
  t = clock() - t;
  printf("Tempo de execucao: %lf", ((double)t)/((CLOCKS_PER_SEC
  ))); //conversão para double
  return 0;
}
