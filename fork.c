#include <unistd.h>
#include <stdio.h>
#include <signal.h>

int main()
{

    int pid= getpid();
    int cpid = fork();

    int i, j, k, ii, jj, kk, N, b;
    N = 4;
    b = 2;
    int A[4][4] = {0};
    int B[4][4] = {{1,2,3,4}, {1,2,3,4}, {1,2,3,4}, {1,2,3,4}};
    int C[4][4] = {{4,3,2,1}, {4,3,2,1}, {4,3,2,1}, {4,3,2,1}};

    if( cpid == 0)
    {
        // child process .  Run your perf stat
        char buf[50];
        sprintf(buf, "sudo perf stat -e instructions:u -p %d   > stat.log 2>&1",pid);
        execl("/bin/sh", "sh", "-c", buf, NULL);

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

    }
    else
    {
        // set the child the leader of its process group
        setpgid(cpid, 0);

        //////////////////////////////////////////////
        // part of program you wanted to perf stat


        ////////////////////////////////////////////////


        ////////////////////////////////////////////////////////////////
        // stop perf stat by killing child process and all its descendants(sh, perf stat etc )
        kill(-cpid, SIGINT);
        ////////////////////////////////////////////////////////////////////


        // rest of the program
        // sleep(2);
     }
}