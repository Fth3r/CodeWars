// solving the 10 minute walk Kata 
#include <vector>
#include <algorithm>

bool isValidWalk(std::vector<char> walk) {
  if (walk.size() == 10 
      && std::count(walk.begin(), walk.end(), 'n') == std::count(walk.begin(), walk.end(), 's')
      && std::count(walk.begin(), walk.end(), 'e') == std::count(walk.begin(), walk.end(), 'w'))
    return true;
  return false;
}
