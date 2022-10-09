// Allocates some amount of memory  and access them in some pattern
// it does show with some radomisation and so that every next adrress is a miss is LLC

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>


void gen_addr(char* temp,char* max_bank, long long stride)
{

   int x;
   //long long count = 0;
   while(temp < max_bank)
   {
      if(rand()%2)
         x = *temp;
      else
         *temp = 1;
      temp += stride;
   }
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

   char* temp = mem;

   // maximum base addr to shift colum
   char* max_col = mem + (1UL<<14);
   long long col_stride = 1UL<<6;
   char* bank_base;
   long long bank_stride = (1UL<<14);
   char* max_bank = mem + (1UL<<19);
   char* col_base;
   char* row_base = mem;
   char* max_row = mem + (1UL<<31);

   for (int i=0; i<6; ++i)
   {
      row_base = mem;
      while(row_base<max_row)
      {
         col_base = row_base;
         max_col = col_base + (1UL<<14);
         while(col_base < max_col)
         {
            max_bank = col_base + (1UL<<19);
            gen_addr(col_base, max_bank, bank_stride);
            col_base += col_stride;
         }
         row_base += row_stride;
      }
   }
   return 0;
}
