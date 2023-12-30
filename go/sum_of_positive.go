//8 kyu kata

package kata

func PositiveSum(numbers []int) int {
  var ret = 0
  for _, value := range numbers {
    if value >= 0 {
      ret += value
    }
  }
  return ret
}

// Found out you can iterate directly over an array
// and grab index, value, etc. as part of the loop.
// this is a very helpful addition to the language!
//
// Also, finally I submitted a solution that meshed with
// what the majority of the others looked like! 