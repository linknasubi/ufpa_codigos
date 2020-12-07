#include <iostream>

struct VecValues{
    private:
        float vector[50];
        int n;
        int ind;
    
    public:
         VecValues(){
            n = 0;
            ind = -1;
        }

        void insereFinal(float value){
            ind += 1;
            vector[ind] = value;
        }
        
        void ordenaElementos(){
            /* Insertion Sort */

            if(ind > -1){
                int i, j;
                float key;  
                for (i = 1; i < ind+1; i++) 
                {  
                    key = vector[i];  
                    j = i - 1;

                    while (j >= 0 && vector[j] > key) 
                    {  
                        vector[j + 1] = vector[j];  
                        j = j - 1;  
                    }  
                    vector[j + 1] = key;  
                } 

                std::cout<<("Vetor devidamente ordenado.\n\n");

            }

            else{
                std::cout<<("Sem valores presentes no vetor.\n\n");
            }

        }

        void exibeElementos(){

            for(int i = 0; i<ind+1; i++)
            {
                std::cout<<(i)<<(" Posicao - ")<<(vector[i])<<("\n");
            }

            std::cout<<("\n");
        }
};



int main(int argc, char * argv[])
{


    VecValues Vector;
    int flag = 0;
    float value;
    int num_values;

    
    while(1){
        if(flag == 0){
            std::cout<<("1 - Inserir elemento no fim.\n")<<("2 - Ordenar os elementos.\n")<<("3 - Exibir elementos.\n")<<("4 - Encerrar programa.\n\n");
            std::cin>>(flag);
            std::cout<<("\n");
        }

        if(flag == 1){
            std::cout<<("Insira a quantidade de elementos a serem inseridos no vetor. O maximo e 50. \n");
            std::cin>>(num_values);

            if(num_values < 0 || num_values > 50){
                    break;
                }


            for(int i = 0; i<num_values; i++){
                std::cout<<("Insira o elemento desejado:");
                std::cin>>(value);

                Vector.insereFinal(value);

            }
            flag = 0;

        }4

        if(flag==2){
            Vector.ordenaElementos();
            flag = 0;
        }

        if(flag==3){
            Vector.exibeElementos();
            flag = 0;
        }

        if(flag == 4){
            break;
        }

        if(flag < 0 || flag > 4){
            break;
        }

    }



}



