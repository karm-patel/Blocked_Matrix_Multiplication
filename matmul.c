#include <stdio.h>




int main(){
int i, j, k, ii, jj, kk, N, b;
N = 4;
b = 2;
int A[4][4] = {0};
int B[4][4] = {{1,2,3,4}, {1,2,3,4}, {1,2,3,4}, {1,2,3,4}};
int C[4][4] = {{4,3,2,1}, {4,3,2,1}, {4,3,2,1}, {4,3,2,1}};

for(i=0; i<N; i=i+b){
    for(j=0; j<N; j=j+b){
        for (k=0; k < N; k=k+b){
            for(ii=i; ii<i+b; ii++){
                for(jj=j; jj < j+b; jj++){
                    for(kk=k; kk < k+b; kk++){
                        A[ii][jj] += B[ii][kk] * C[kk][jj];
                    }
                }
            }
        }
    }
}

for(i=0; i<N; i+=1){
    for(j=0; j<N; j+=1){
        printf("%d ", A[i][j]);
    }
    printf("\n");
}
return 0;
}