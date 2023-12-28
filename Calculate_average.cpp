// solving the calculate averages 8kyu kata
#include <vector>

double calcAverage(const std::vector<int>& val){
  double ret = 0.0;
  if (val.size()) {
    for (int i: val) ret += i;
    return (ret/(val.size()));
  }
  return 0;
}
