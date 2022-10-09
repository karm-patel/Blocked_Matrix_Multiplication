// Allocates some amount of memory and access some addresses.
// it does show with some radomisation and so that every next adrress is a miss is LLC

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

int main(int argc, char **argv){
	char *mem;
	long long sizeBytes = 1UL<<31;
	long long row_stride = 1UL<<19;
	mem = (char *)mmap(NULL, sizeBytes, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
	if(!mem)
	{
		printf("Could not allocate the memory\n try to close other apllications and run again");
	}

	//memset(mem, 1, sizeBytes);
	for (long long i=0; i<((1UL<<27)+(1UL<<26)) ; ++i)
	{
		int x;
		if(rand()%2)
			x = *(mem + rand());
		else
			*(mem + rand()) = 10;
	}
	
	return 0;
}
