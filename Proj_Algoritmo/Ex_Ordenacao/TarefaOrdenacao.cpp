#include <iostream>
#include <stdlib.h>
#include <time.h> //clock(), CLOCKS_PER_SEC e clock_t
using namespace std;

typedef int tDado;

tDado vet[200000];


/* 

NOME DO/A ALUNO/A: Gabriel Oliveira Aragão

tarefa 1)  completar a função quicksort abaixo

Já está sendo realizado o processo separação dos elementos
- foi escolhodo com pivo o elemento do meio
- os menores que o pivô já se encontram entre esq e j
- os maiores que o pivô já se encontram entre i e dir

Chamar a função recursiva para ordenar essas partições 
Qual a condição de parada? ( momento em que já não se deve chamar a recursividade para as 
partições)


2) Desenvolver a função selecao recursivamente.


3) Variar o valor de n (elementos do vetor) e observar o tempo decorrido para ordenação com 
quicksort e seleção. Anotar os valores em milissegundos e avaliar o que acontece com  crescimento do vetor. 
Informe os valores observados ao aumentar n (para os dois algoritmos) e explique esses dados.





*/

void quicksort (tDado v[],int esq, int dir) {
   int i,j;
   tDado pivo, aux;
   
   i = esq; j = dir;
   pivo = v[(esq+dir) / 2];     // pivô será o elemento do meio
   // separar em duas partições: menores a esquerda e maiores a direita do pivô
   while (i <= j) {
      while(v[i] < pivo) i++;
      while(v[j] > pivo) j--;
      if (i<=j) {
         aux = v[i];
         v[i]=v[j];
         v[j] = aux;
         i++;
         j--;
      } 
    }

   //  ordenar as partições   
   // ( completar) 
   //  ...........

   if(j > esq){
       quicksort(v, esq, j);
   }
   
   if(i < dir){
      quicksort(v, i, dir);
   }

    

   
}

// desenvolver recursivamente - esq e dir delimitam a parte a ser ordenada
void selecao(tDado v[], int esq, int dir) {
   

   int aux, less;
   less = esq;

     //  estabelecer uma condição de parada

   if(esq == dir){
      return;
   }

     // identificar o menor e colocá-lo no início da faixa que vai de esq até dir

   for(aux=esq; aux < dir; aux++){
      if(v[less] > v[aux]){
         less = aux;
      }
   }


   if(less != esq){
      aux = v[esq];
      v[esq] =  v[less];
      v[less] = aux;
   }

   selecao(v, esq+1, dir);
     
     // chamada recursiva para ordenar a parte remanescente


}



int main ()
{
   int n, m; // tamanho lógico (número de casas ocupadas) do vetor
   char continua;
   clock_t t1,t2, dif; //variáveis para calcular o tempo decorrido na execução

   do {
      cout <<  "Informe o número de elementos: ";
      cin >> n;
      cout << "\nQuick Sort - 1\nSelection Sort - 2\n";
      cin>> m;
   
       
      // gerar n números aleatórios entre 1 e n
      for (int i=0; i<n; i++)
         vet[i] = rand() % n + 1;    

      //exibir o vetor no estado inicial  
      for (int i=0; i<n; i++)
         cout<< vet[i] << " ";
      cout<< endl;
   
      t1 = clock(); // registra instante do início
   
      // ALTERNAR OS MÉTODOS... 
      if(m == 1){

         quicksort(vet, 0, n-1);
      }

      if(m == 2){

         selecao(vet, 0, n);
      }
   
      t2 = clock();     // registra instante do final 
      dif = t2-t1;      // intervalo decorrido entre t1 e t2 em milissegundos
   
      //exibir o vetor ordenado 
      for (int i=0; i<n; i++)
         cout<< vet[i] << "  ";
      cout<< endl;

      // informar tempo decorrido em milissegundos
      double tempoExec = ((double) dif) / (CLOCKS_PER_SEC / 1000);  //conversão para milissegundos    
      cout << "Tempo de execucao: " << tempoExec << "ms." << endl; 
      
      cout <<  "Quer continuar? (S/N) ";
      cin >> continua;
             
      
   } while (continua == 'S' || continua == 's');



   
}
