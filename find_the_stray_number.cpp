// 7 kyu kata
int stray(std::vector<int> n) {
    for (int i : n)
    {
      if (std::count(n.begin(), n.end(), i) == 1)
        return i;
    }
}
