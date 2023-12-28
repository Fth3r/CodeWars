// solving the 6 kyu bit counting kata
#include <bitset>

unsigned int countBits(unsigned long long num){
  
  std::bitset<64> bs(num);
  return bs.count();
}
