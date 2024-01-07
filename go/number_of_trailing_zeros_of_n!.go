package kata

import "math"

func Zeros(n int) int {
  k,res := 0,0
  num := n
  for num >= 5 {
    num /= 5
    k++
  }  
  for i := 1; i <= k; i++ {
    res += int(n/int(math.Pow(5,float64(i))))
  }
  return res
}
