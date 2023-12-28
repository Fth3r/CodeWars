// solving the simple pig latin 5 kyu kata
#include <string>
#include <iostream>
#include <sstream>

std::string pig_it(std::string str)
{
  std::istringstream ss(str);
  std::string ret;
  
  do {
    std::string word;
    ss >> word;
    if (word.find("!") != std::string::npos ||
        word.find(",") != std::string::npos ||
        word.find(".") != std::string::npos ||
        word.find("?") != std::string::npos)
    {
      ret += word + " ";
      continue;
    }
    
    word += word[0];
    word += "ay ";
    word = word.erase(0, 1);
    
    ret += word;
    
  } while (ss);
  
  if (ret.find(" ay ")) return ret.erase(ret.find(" ay "));
  else return ret;
}
