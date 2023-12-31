// 8 kyu kata

package kata


func CountBy(x, n int) []int {
  var ret []int
  for i := 1; i <= n; i++ { ret = append(ret, (x * i)) }
  return ret
}

// This was a pretty standard solution, and it seems like this is 
// the way most people solved it. Which means there wasn't some gotcha
// solution that a newbie like me would miss. 
//
// I am still getting used to :=, slices, and the append function