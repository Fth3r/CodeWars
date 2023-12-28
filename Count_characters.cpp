// solving the 6 kyu counting characters in your string kata
#include <map>
#include <string>

std::map<char, unsigned> count(const std::string& string) {
  
    std::map<char, unsigned> counter;
  
    for (auto i : string)
    {
        if (counter.count(i) == 0) counter.insert(std::pair<char, unsigned>(i, 1));
        else ++counter.at(i);
    }
    return counter;
}
