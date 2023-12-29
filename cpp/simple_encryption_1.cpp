// 6 kyu kata
#include <math.h>

std::string encrypt(std::string text, int n)
{
  // If the string is empty or we are asked to iterate < 1 times, just return the string
  if (n <= 0 || text.length() == 0) { return text; }
  
  std::string odds;
  std::string evens;
  std::string::iterator it = text.begin();

  // Use ternary operation with a for loop to go over text once and split out odd and even indices
  for (; it < text.end(); ++it) { std::distance(text.begin(), it) % 2 == 0 ? evens += *it : odds += *it; }

  text = odds + evens; 
  // Use ternary operation again to recursively operate until n == 1
  return n == 1 ? text : text = encrypt(text, --n); 
}

std::string decrypt(std::string text, int n)
{
  // Same as above
  if (n < 1 || text.length() == 0) { return text; }
  
  std::string::iterator it = text.begin();
  std::size_t offset = ceil(text.size()/2);
  std::string str;

  // Since we got an offset to half of the string, we only need to loop over half the indices
  for (size_t i = 0; i < offset; i++ ) {
    // it + offset gets us the evens
    str += *(it + offset);
    // it gets us the odds, and we post increment
    str += *it++;
    }

  // If the original string length is odd, we will be missing the last character at this point, so get it and append
  if (text.length() % 2 != 0) { str += text.back(); }

  // same as the return above
  return n == 1 ? str : str = decrypt(str, --n);
}
