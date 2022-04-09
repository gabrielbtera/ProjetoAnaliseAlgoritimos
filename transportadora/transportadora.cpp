#include <iostream>
#include <ctime>
#include <vector>

using namespace std;

uint32_t * vetorTamanhon(uint32_t n) {

   uint32_t* r = (uint32_t*)(malloc(n * sizeof(uint32_t)));

   
   for (int i = 0; i < n; ++i) {
      r[i] = i;
   }

   return r;
}

int main () {

  
   uint32_t *p;
   uint32_t n = 100;

   p = vetorTamanhon(n);
   
   for ( int i = 0; i < n; i++ ) {
      cout << "*(p + " << i << ") : ";
      cout << *(p + i) << endl;
   }

   return 0;
}