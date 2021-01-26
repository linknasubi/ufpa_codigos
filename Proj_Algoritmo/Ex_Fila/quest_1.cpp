#include <iostream>
#include <bits/stdc++.h>


using namespace std;

int len_node = 0;


class Node  
{  
    public: 
    int data;  
    Node *next;  



    Node* create(int data, Node* tail_ref){

        Node* node = NULL;
        node = new Node();

        node -> data = data;
        node -> next = tail_ref;

        return node;

    }



};  


Node* head_ref = head_ref -> create(NULL, NULL);





class Descriptor
{

    public:
    Node *starts;
    Node *finals;



    Descriptor* init(Node *inicio, Node*fim){

        Descriptor *descr = NULL;
        descr = new Descriptor();

        descr -> starts = inicio;
        descr -> finals = fim;

    }


};


Descriptor *descr = descr -> init(NULL, head_ref);


bool checkList(){
    if(descr->starts == NULL){
        return false;
    }
    else{
        return true;
    }
}


void nodeAppending(){
    int n;
    char ch;
    Node* temp = head_ref;
    while(temp != NULL){


        cout<<"Insira o valor  ";
        cin>>temp->data;


        cout<<"Deseja continuar(s/n)  ";
        cin>>ch;
        
        if(ch=='S' || ch == 's'){
            

            //cout<<temp<<'\n';

            temp->next = new Node; 
            temp = temp->next;
            descr->starts = temp;
        }
        
        else{
            
            temp->next = NULL;
            temp = NULL;
        }

    }
}


void printList(Node* n) { 
        while (n != NULL) {
            len_node += 1;
            std::cout << n->data << " "; 
            n = n->next; 
        }
        std::cout<<"\n";
}

bool nodeRemoving(){


    if(checkList() == true){

        Node* current = descr->finals;
        descr->finals = descr->finals->next;
        free(current);

        return true;

    }
    else{
        return false;
    }




}


int main(int argc, char * argv[])   {



    int quest = 2;
    
    while (quest > 0 && quest < 11){
        std::cout<<"\n===============\nValores presentes na fila: ";
        printList(descr->finals);
        std::cout<<"\n===============\n";
        std::cout<<"Escolha a opcao desejada.\n";
        std::cout<<"1 - Enfileirar elemento\n2 - Informar o elemento do inicio da fila\n3 - Desenfileirar elemento\n4 - Verificar se a fila esta vazia\n5 - Exibir a fila\n";
        std::cin>>quest;

        if(quest == 1){
            nodeAppending();
        }

        if(quest==2){

            cout<<(descr->finals->data);
        }

        if(quest==3){

            nodeRemoving();

        }

        if(quest==4){

            checkList();

        }


        if(quest==5){

            printList(descr->finals);

        }

        if(quest==6){
            quest = 30;
        }


    }

   
    return 0;
}