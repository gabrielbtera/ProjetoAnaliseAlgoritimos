#include <stdio.h>
#include <stdlib.h>


int main (){

    char alfabeto[26] = {'a', 'b', 'c', 'd', 'e', 'f','g','h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    char criptografado[26] = {'a', 'b', 'c', 'd', 'e', 'f','g','h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    char palavra[20];

    int rotacao = 11, cont = 0;

    char palavra2[26];

    for(int i =0; i < 26; i++){
            if (i + rotacao < 26)
                criptografado[i] = alfabeto[rotacao + i];
            else{
                criptografado[i] = alfabeto[cont];
                printf("%c\n", alfabeto[cont]);

                cont++;
            }
    }

    for (int i = 0 ; i < 26; i++){

            printf("%c", criptografado[i]);
    }
    printf("\n");

     for (int i = 0 ; i < 26; i++){
        printf("%c", alfabeto[i]);
     }

     scanf("%s", palavra2);

     for (int i = 0; i < 8; i++){
            for (int j =0 ; j < 26; j ++){
                 if(palavra2[i] == alfabeto[j]){
                        printf("%c", criptografado[j]);

                 }
            }

     }


    return 0;

}
