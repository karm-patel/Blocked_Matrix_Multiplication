//i,k,j
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int N = 8192;
double A[8192][8192];
double array1[8192][8192];
double array2[8192][8192];
int B = 128;

void init(){

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
}

void multiplication(){
for(int k=0; k<N; k=k+B)
	{	
		for(int i=0; i<N; i=i+B){
 			
 			for (int j=0; j < N; j=j+B){
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



