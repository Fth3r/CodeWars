// solving the 6 kyu find the parity outlier kata
int FindOutlier(std::vector<int> arr)
{
  int result = 0;
  int num = 0;
  
  bool even = ((arr[0] % 2 == 0 && arr[1] % 2 == 0) ||
               (arr[0] % 2 == 0 && arr[2] % 2 == 0) ||
               (arr[1] % 2 == 0 && arr[2] % 2 == 0) ? true : false);
  
  if (even)
  {
    for (auto i : arr)
      if (i % 2 != 0) num = i;
    result = num;
  }
  else if (!even)
  {
    for (auto i : arr)
      if (i % 2 == 0) num = i;
    result = num;
  }
  
  return result;
}
