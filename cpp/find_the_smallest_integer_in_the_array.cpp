// 8 kyu kata
#include <vector> 

int findSmallest(std::vector <int> list)
{
  sort(list.begin(), list.end());
  return list[0] ;
}
