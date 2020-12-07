#include <iostream>
using namespace std;

int* v1;
int* v2;


int* reverFunction(int (&arr)[7]){


    static int reverArray[7];

    int aux = 0;

    for(int i=0; i<7; i++){

        aux = 7 - i;
        reverArray[i] = arr[aux];

    }


    return reverArray;
}



int* rec_reverFunction(int(&arr)[7], int init, int final){

    if(init == final){
        return arr;
    }

    int aux = arr[init];
    arr[init] = arr[final];
    arr[final] = aux;

    

    return rec_reverFunction(arr, init + 1, final - 1);

}


int evenSum(int arr[], int size){

  int sum = 0;

  for(int i = 0; i < size; i+=2){
    sum += arr[i];
  }

  return sum;
}


int factorial(int n){

  if(n == 1){
    return 1;
  }

  return factorial(n-1)*n;
}


int* fibonacci(int n){


    int arr[n];
    arr[0] = 0;
    arr[1] = 1;
    for(int i = 2; i<n+1; i++){
      arr[i] = arr[i-1] + arr[i-2];


    }

    return arr;

}


int* rowSum(int matr[5][5]){
    int sum = 0;
    static int arr[5];


    for(int j = 0; j < 5; j++){
      for(int i = 0; i < 5; i++){
        sum += matr[i][j];
      }

      arr[j] = sum;
      sum = 0;
    }

    return arr;
  }


int* colSum(int matr[5][5]){
    int sum = 0;
    static int arr[5];


    for(int i = 0; i < 5; i++){
      for(int j = 0; j < 5; j++){
        sum += matr[i][j];
      }

      arr[i] = sum;
      sum = 0;
    }

  return arr;
}

void genSum(int matr[5][5]){
  v1 = rowSum(matr);
  v2 = colSum(matr);


}

int diagonalSum(int matr[5][5]){
  int sum = 0;

  for(int i = 0; i<5; i++){
    sum += matr[i][i];
  }

  return sum;
}

int overdiagonalSum(int matr[5][5]){
  int sum = 0;

  for(int i = 0; i < 5; i++){
    for(int j = 5; j > i;  j--){
      sum += matr[i][j];
    }
  }

  return sum;

}

int underdiagonalSum(int matr[5][5]){
  int sum = 0;

  for(int j = 0; j < 5; j++){
    for(int i = 5; i > j; i--){
      sum += matr[i][j];
    }
  }

  return sum;

}


int sec_diagonalSum(int matr[5][5]){
  int sum = 0;
  int j = 4;

  for(int i = 0; i<5; i++){
    j -= i;
    sum += matr[i][j];
  }

  return sum;
}



int oversec_diagonalSum(int matr[5][5]){
  int sum = 0;

  for(int i = 0; i < 5; i++){
    for(int j = 0; j < 5;  j++){
      if((j+i)<4){

        sum += matr[i][j];
      }
    }
  }

  return sum;

}


int undersec_diagonalSum(int matr[5][5]){
  int sum = 0;

  for(int i = 0; i < 5; i++){
    for(int j = 0; j < 5;  j++){
      if((j+i)>4){

        sum += matr[i][j];
      }
    }
  }

  return sum;

}


void pascalTriangle(int n){


  int matrix[n][n];
  std::cout<<'\n';

  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){

      matrix[i][j] = 0;

      if(j == 0){
        matrix[i][j] = 1;
      }
    }
    matrix[i][i] = 1;

  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < i+1; j++){
      if(matrix[i][j] == 0){
        matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1];
      }
      std::cout<<matrix[i][j]<<' ';
    }
    std::cout<<'\n';
  }

}



//COLOCAR UM STD::COUT EM TODAS FUNÇÕES


int main() {
  cout << "Hello World!";



    int vec[7] = {5,8,1,0,9,5,3};
    int matrix[5][5] = {{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}};


    int* rev_vec = reverFunction(vec);
    int* teste = rec_reverFunction(vec, 0, 6);
    

    int sum = evenSum(vec, 7);


    int fac = factorial(4);

    int* fib = fibonacci(6);

    int* rowsum = rowSum(matrix);

    int* colsum = colSum(matrix);

    genSum(matrix);

    int diagonalsum = diagonalSum(matrix);

    pascalTriangle(5);

    std::cout<<'\n'<<diagonalsum;



  return 0;
}