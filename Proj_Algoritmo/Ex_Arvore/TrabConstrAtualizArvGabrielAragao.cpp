/* 

TRABALHO
ENVIAR ATÉ 22/02/2021 

O programa já contém uma função (mostrada na aula) para criar uma árvore completa:
-  os elementos são fornecidos em pré-ordem
- quando não há mais filhos, à esquerda ou à direita, deve-se fornecer o caractere que simboliza NULL ( "/" )  para indicar isso.

Criar duas funções adicionais (inserindo no menu do programa):

- Inserção de um valor "val"  em um filho à esquerda de determinado nó (com determinado conteúdo) 

- Inserção de um valor "val"  em um filho à direita de determinado nó (com determinado conteúdo) 
(são funções de retorno do tipo bool - se a tarefa foi realizada ou é impossível)

Obs: decompor o problema, conforme discutido em sala: uma função que retorne o 
ponteiro para o nó em questão (ou NULL se ele não existir)

Sugestão: quando forem testar, desenhem em papel a árvore. Criem a árvore e explorem as opções inserir a esquerda (ou a direita)
          de determinado nó - acompanhem se a evolução da árvore está correta com as funções de percurso que exibem os nós em
          pré-ordem, pós-ordem ou central. 
          
*/



#include <iostream>
using namespace std;
 
typedef char tDado;

struct NoArvBin
{
    NoArvBin * esq;  // ponteiro para a subárvora da esquerda
    tDado dado;      // dado armazenado
    NoArvBin * dir;  // ponteiro para a subárvora da direita
};


typedef NoArvBin * ptNo;      // Tipo ptNo - definição de ponteiros para nós de uma árvore

void construir_arvore(ptNo & p ) {
   tDado x;   
   
   cin >> x;
   if (x == '/') {        // não construir nó - não há subárvore naquele ponto
      p = NULL;
      return;
   }
   // alocar o nó
   p = new NoArvBin;
   p->dado = x;
  
   cout << "Ins. a esquerda de " << p->dado << ". " << endl;
   construir_arvore(p->esq );
   cout << "Ins. a direita de " << p->dado << ". " << endl;   
   construir_arvore(p->dir);
}   
   


void visitar (ptNo p)
{
   cout << p->dado << "  ";
}

void percorrer_pre_ordem(ptNo p )
{
      if (p!= NULL)
      {
            visitar(p);
            percorrer_pre_ordem(p->esq );
            percorrer_pre_ordem(p->dir );
      }
}

void percorrer_pos_ordem(ptNo p )
{
      if (p!= NULL)
      {
            percorrer_pos_ordem(p->esq );
            percorrer_pos_ordem(p->dir );
            visitar(p);
      }
}


void percorrer_ordem_central(ptNo p )
{
      if (p!= NULL)
      {
            percorrer_ordem_central(p->esq );
            visitar(p);
            percorrer_ordem_central(p->dir );
      }
}

void liberarArvore(ptNo &p)
{
     if (p != NULL)   // condiçao de parada
     {
         liberarArvore(p->esq);    // libera toda a subárvore da esquerda
         liberarArvore(p->dir);    // libera toda a subárvore da direita
         cout << "Liberando no contendo o elemento " << p->dado << endl;         
         delete p;
         p = NULL;
     }        
}

ptNo buscArvore(ptNo &p, int node){

      ptNo aux;

      if(p->dado == node){
            return p;
      }
      
      aux = buscArvore(p->esq, node);

      if(aux == NULL){
            aux = buscArvore(p->dir, node);

      }

}

bool insEsquerda(ptNo &p, int node, int val)
{

      ptNo nodeSearched;

      nodeSearched = buscArvore(p, node);

      if(nodeSearched == NULL){
            cout<<"\nNo inexistente.\n";
            return false;
      }

      if(nodeSearched->esq != NULL){
            cout<<"\nNo ocupado.\n";
            return false;
      }


      ptNo pNew = NULL;
      pNew = new NoArvBin;
      nodeSearched->esq = pNew; 
      pNew->dado = val;
      pNew->dir = NULL;
      pNew->esq = NULL;



      return true;

}


bool insDireita(ptNo &p, int node, int val)
{

      ptNo nodeSearched;

      nodeSearched = buscArvore(p, node);

      if(nodeSearched == NULL){
            cout<<"\nNo inexistente.\n";
            return false;
      }
            if(nodeSearched->dir != NULL){
            cout<<"\nNo ocupado.\n";
            return false;
      }


      ptNo pNew = NULL;
      pNew = new NoArvBin;
      nodeSearched->dir = pNew; 
      pNew->dado = val;
      pNew->dir = NULL;
      pNew->esq = NULL;



      return true;

}

void  exibirMenu( )
{
      cout << "1 -  Construir a arvore" << endl;
      cout << "2 -  Mostrar a arvore em pre-ordem"  << endl;
      cout << "3 -  Mostrar a arvore em pos-ordem"  << endl;
      cout << "4 -  Mostrar a arvore em ordem central"  << endl;
      cout << "5 -  Inserir elemento a esquerda"  << endl;
      cout << "6 -  Inserir elemento a direita"  << endl;
      cout << "7 -  Encerrar programa"  << endl << endl;
      cout << "Escolha uma opcao:  " ;
}


int main ()
{
   ptNo p = NULL;    // inicializar árvore
   tDado node, val;
   int opc;
   bool fimProg = false;
   do 
   {
       exibirMenu( );
       cin >> opc;
       switch (opc)
       {
            case 1:
                 construir_arvore(p);
                 break;
            case 2:
                 percorrer_pre_ordem(p);
                 cout << endl;
                 break;
            case 3:
                 percorrer_pos_ordem(p);
                 cout << endl;
                 break;
            case 4:
                 percorrer_ordem_central(p);
                 cout << endl;
                 break;
            case 5:
                  
                  cout<<"Insira o no para se inserir a esquerda: ";
                  cin>>node;
                  cout<<"Insira o conteudo do no: ";
                  cin>>val;
                  insEsquerda(p, node, val);  
                  break;
            case 6:
                  cout<<"Insira o no para se inserir a direita: ";
                  cin>>node;
                  cout<<"Insira o conteudo do no: ";
                  cin>>val;
                  insDireita(p, node, val);  
                  break;    
            case 7:
                 fimProg = true;
                 //break;
       }
   } while (! fimProg);
   liberarArvore(p);

}
