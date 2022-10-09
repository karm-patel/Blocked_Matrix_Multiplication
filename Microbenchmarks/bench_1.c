// Allocates some amount of memory and generate row interleaving addresses
// it does show with some radomisation and so that every next adrress is a miss is LLC

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>


void gen_addr(char* temp,char* base,long long size, long long stride)
{

	//long long count = 0;
	while(temp < (base + size))
	{
		int x;
		//printf("%lx\n", temp);
		if(rand()%2)
			x = *temp;
		else
			*temp = 1;
		
		temp += stride;
		//++count;

	}
	//return count;
}


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

	char* temp = mem;
	long long count = 0;
	//printf("%lld", count);

	// maximum base addr to shift colum
	char* max_col = mem + (1UL<<14);
	long long col_stride = 1UL<<6;
	char* bank_base;
	long long bank_stride = (1UL<<14);
	char* max_bank = mem + (1UL<<19);
	char* col_base;

	for (int i=0; i<6; ++i)
	{
		bank_base = mem;
		while(bank_base<max_bank)
		{
			col_base = bank_base;
			max_col = col_base + (1UL<<14);
			while(col_base < max_col)
			{
				gen_addr(col_base, mem,sizeBytes, row_stride);
				col_base += col_stride;
			}
			bank_base += bank_stride;
		}
	}
	return 0;
}

