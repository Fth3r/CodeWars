// solving the 6 kyu convert string to camel case kata
#include <string>
#import <algorithm>


std::string to_camel_case(std::string text) {
  std::cout << text << std::endl;
  std::vector<int> ind;
  for (auto x : text)
  {
    if (x == '-' || x == '_')
    {
      int i = text.find(x);
      ind.push_back(i);
      text.erase(i, 1);
    }
  }
  
  for (auto i : ind)
  {
    text[i] = toupper(text[i]);
  }
  return text;
}
