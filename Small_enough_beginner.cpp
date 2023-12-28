// solving the 7 kyu small enough? - beginner kata
#include <vector>
#include <iostream>

bool small_enough(std::vector<int> arr, int limit) {
    if (arr.size() == 0) return true;
    std::sort(arr.begin(), arr.end(), std::greater<int>());
    return (arr.at(0) <= limit);
}
