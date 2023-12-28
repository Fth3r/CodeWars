// solving the 7 kyu shortest word kata
#include <string>
#include <vector>
#include <algorithm>

int find_short(std::string str)
{ 
	std::istringstream ss(str);
	std::string word;

  // splitting the std::string into a std::vector<std::string>
	std::vector<std::string> words;
	while(std::getline(ss, word, ' '))
		words.push_back(word);
  
  // sort the std::vector by std::string.size() using a lambda function
  std::sort(words.begin(), words.end(), [](std::string a, std::string b) { return a.size() < b.size(); });
  
  // return the first element in std::vector, as it will be the shortest
  return words[0].size();
}
