//j,i,k
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int N = 4;
double A[4][4];
double array1[4][4];
double array2[4][4];
int B = 2;

void init(){

	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			array1[i][j] = (rand() % 10) +1;
            printf(" ");
		}
	}
	
	
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			array2[i][j] = (rand() % 10) + 1;
		}
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
    srand((unsigned) time(&t1)); 

	init();	
	multiplication();
 	
 	return 0;
}



