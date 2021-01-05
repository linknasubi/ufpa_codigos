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



Node* node_4 = node_4 -> create(9 , NULL);
Node* node_3 = node_3 -> create(1 , node_4);
Node* node_2 = node_2 -> create(7 , node_3);
Node* head = head -> create(4 , node_2);


Node* head_ref = head_ref -> create(NULL, NULL);


//#define INT_MIN -2147483648

void printList(Node* n) { 
        while (n != NULL) {
            len_node += 1;
            std::cout << n->data << " "; 
            n = n->next; 
        }
        std::cout<<"\n";
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
        
        temp->next = new Node; 
        temp = temp->next;
    }
    
    else{
        
        temp->next = NULL;
        temp = NULL;
    }

  }
}

void push(int new_data)  {  


    if(head_ref->data == NULL){

        head_ref->data = new_data;
        head_ref->next = NULL;
    }

    else{

        Node* new_node = new Node();
        new_node->data = new_data;
        new_node->next = head_ref;  
        head_ref = new_node;

    }

}


bool insertNode(int new_data, Node* prev_node)   { 
    
    if (prev_node == NULL)   
    {   
        std::cout << "Nó inexistente.";   
        return false;   
    }  
    
    else{

        Node* new_node = new Node();  
        new_node->data = new_data;   
        new_node->next = prev_node->next;   
        prev_node->next = new_node;   

        return true;
    }



}


bool insertKNode(int new_data, int n)   {


    int aux = 1;
    Node* aux_node = head_ref;

    if(n > len_node-1 || n <= 0){
        std::cout<<"No inexistente.\n";
        return false;
    }



    else{

        while (aux != n) { 
            aux += 1;
            aux_node = aux_node->next; 
            
            }


        Node* new_node = new Node();  
        new_node->data = new_data;   
        new_node->next = aux_node->next;   
        aux_node->next = new_node;  

        std::cout<<"\n";

        return true;
    }



}


void multPenElems() {
    int val;

    Node* q;

    q = node_3;

    val = q->data * q->next->data;

    std::cout<<val<<'\n';

}


int returnValue(int n)  {

    int aux = 0;
    int val;
    Node* aux_node = head_ref;

    if(n > len_node-1){
        std::cout<<"No inexistente.";
        return INT_MIN;
    }

    while (aux != n) { 
        aux += 1;
        aux_node = aux_node->next; 
        
        }

    val = aux_node->data;

    std::cout<<"\n";

    return val;
}


void deleteNodes()  {  
      
    Node* current = head_ref;  
    Node* next;  
    
    while (current != NULL)  
    {  
        next = current->next;  
        free(current);  
        current = next;  
    }  
    head_ref = NULL;  
} 


void deleteNodesR(Node* &aux) 
{ 
    if (aux->next == NULL){
        head_ref = NULL;
        return;
    } 

    deleteNodesR(aux->next);
    free(aux); 


} 
  


int main(int argc, char * argv[])   {

    int quest = 2;
    


    while (quest > 0 && quest < 11){
        std::cout<<"===============\nValores presentes na lista: ";
        printList(head_ref);
        std::cout<<"===============\n";
        std::cout<<"Escolha a opcao desejada.\n";
        std::cout<<"1 - Inicializar os valores de uma lista encadeada\n2 - Questao 1\n3 - Questao 2\n4 - Questao 3\n5 - Questao 4\n6 - Questao 5\n";
        std::cout<<"7 - Questao 6\n8 - Questao 7\n9 - Questao 8\n10 - Questao - 9\n";
        std::cin>>quest;

        if(quest == 1){
            nodeAppending();
        }

        if(quest==2){

            Node* new_node = new Node();  
            new_node->data = 2;
            new_node->next = head;  
            head = new_node;
            printList(head);
        }

        if(quest==3){

            //Questão 2
            multPenElems();

        }

        if(quest==4){

            //Questão 3
            int val = (node_3->data + node_4->data)/2;
            bool flag = insertNode(val, node_3);
            printList(head);

        }


        if(quest==5){

            //Questão 4
            std::cout<<"Resposta: ";
            printList(head_ref);   

        }


        if(quest==6){

            //Questão 5
            std::cout<<head_ref<<'\n';
            int x = 35;
            push(x);
            std::cout<<head_ref<<'\n';
            std::cout<<"Resposta: ";
            printList(head_ref);
        }


        if(quest==7){


            //Questão 6

            int val = returnValue(5);
            std::cout<<"Resposta: "<<val<<"\n";
        }

        if(quest==8){

            //Questão 7

             int x = 410;

             bool flag = insertKNode(x, 0);
             std::cout<<"Resposta: "<<flag<<"\n";


            
        }

        if(quest==9){

            //Questão 8
            deleteNodes();
            
        }

        if(quest==10){

            //Questão 9
            deleteNodesR(head_ref);
            
        }

    }
    


    return 0;
}