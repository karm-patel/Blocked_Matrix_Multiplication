#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>


int N = 128;
float A[128][128];
int array1[128][128];
int array2[128][128];
int B = 32;
// int N = 4;
// float A[4][4];
// int array1[4][4];
// int array2[4][4];

void printArray(float A[N][N],int N){
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			printf("%f ",a[i][j] );
		}
		printf("\n");
	}
}

void multiplication(){
for(int i=0; i<N; i=i+B)
	{	
		for(int j=0; j<N; j=j+B){
 			
 			for (int k=0; k < N; k=k+B){
 				for(int ii=i; ii<i+B; ii++){
 					for(int jj=j; jj < j+B; jj++){
 						for(int kk=k; kk < k+B; kk++){
 							A[ii][jj] += array1[ii][kk] * array2[kk][jj];
 							}
 						}
 					}
 				}
 			}
 							
 	} 
}

int main(){
	
	time_t t1; 
    	srand (128); 
	
	
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			array1[i][j] = (rand() % 10) +1;
		}
	}
	
	
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			array2[i][j] = (rand() % 10) + 1;
		}
	}
	
	
	
	multiplication();
 //	printArray(A,N);
 	
 	return 0;
}



