// 8 kyu kata
#include <vector>

bool betterThanAverage(std::vector<int> classPoints, int yourPoints) {
  int size = classPoints.size() + 1;
  int total = yourPoints;
  
  for (int i : classPoints)
    total += i;
  
  float avg = total / size;
  
  if (yourPoints > avg)
    return true;
  else
    {
    return false;
  }
}
