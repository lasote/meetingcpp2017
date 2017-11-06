#include <iostream>
#include "a.h"
#include "b.h"

void b(){
 a();
 #ifdef _WIN64
   std::cout << "LibB 64 bits\n";
 #else
   std::cout << "LibB 32 bits\n";
 #endif
}

