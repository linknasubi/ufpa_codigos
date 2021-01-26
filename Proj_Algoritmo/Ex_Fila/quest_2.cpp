#include <iostream>
#include <bits/stdc++.h>


using namespace std; 


class Queue
{ 
    public:
        int rear, front; 

        int size; 
        int *arr; 
  
    Queue(int s) 
    { 
       front = rear = -1; 
       size = s; 
       arr = new int[s]; 
    } 
  
    void enQueue(int value); 
    bool deQueue(); 
    void displayQueue();
    void displayFQueue();
    void checkEmpty();

}; 
  
  

    void Queue::enQueue(int value) 
    { 
        if ((front == 0 && rear == size-1) || 
                (rear == (front-1)%(size-1))) 
        { 
            cout<<("Fila Cheia"); 
            return; 
        } 
    
        else if (front == -1) 
        { 
            front = rear = 0; 
            arr[rear] = value; 
        } 
    
        else if (rear == size-1 && front != 0) 
        { 
            rear = 0; 
            arr[rear] = value; 
        } 
    
        else
        { 
            rear++; 
            arr[rear] = value; 
        } 
    } 
    

    bool Queue::deQueue() 
    { 
        if (front == -1) 
        { 
            cout<<("\nFila Vazia"); 
            return false; 
        } 
    
        int data = arr[front]; 
        arr[front] = -1; 
        if (front == rear) 
        { 
            front = -1; 
            rear = -1; 
        } 
        else if (front == size-1) 
            front = 0; 
        else
            front++; 
    

    } 
    

    void Queue::displayQueue() 
    { 
        if (front == -1) 
        { 
            cout<<("Fila Vazia\n"); 
            return; 
        } 
        if (rear >= front) 
        { 
            for (int i = front; i <= rear; i++) 
                cout<<(" %d ",arr[i]); 
        } 
        else
        { 
            for (int i = front; i < size; i++) 
                cout<<(" %d ", arr[i]); 
    
            for (int i = 0; i <= rear; i++) 
                cout<<(" %d ", arr[i]); 
        }
    }

    void Queue::displayFQueue()
    {
        if (front == -1) 
        { 
            cout<<(INT_MIN); 
            return; 
        }

        else
        {
            cout<<('\n%d ', arr[0]);
        }
    }

    void Queue::checkEmpty() 
    { 
        if (front == -1) 
        { 
            cout<<("\nFila Vazia"); 
            return; 
        } 

        else
        { 
            cout<<("\nFila Não Vazia"); 
            return; 
        }
} 
  

int main() 
{ 

    int value;
    Queue q(6); 

    int quest = 2;
    
    while (quest > 0 && quest < 11){
        std::cout<<"\n===============\nValores presentes na fila: ";
        q.displayQueue();
        std::cout<<"\n===============\n";
        std::cout<<"Escolha a opcao desejada.\n";
        std::cout<<"1 - Enfileirar elemento\n2 - Informar o elemento do inicio da fila\n3 - Desenfileirar elemento\n4 - Verificar se a fila esta vazia\n5 - Exibir a fila\n";
        std::cin>>quest;

        if(quest == 1){
            cout<<"Insira o valor para se enfileirar: ";
            cin>>value;
            q.enQueue(value);
        }

        if(quest==2){

            q.displayFQueue();
        }

        if(quest==3){

            cout<<("\nValor Deletado = %d", q.deQueue()); 

        }

        if(quest==4){

            q.checkEmpty();

        }


        if(quest==5){

            q.displayQueue();

        }

        if(quest==6){
            quest = 30;
        }


    }

    return 0; 
} 