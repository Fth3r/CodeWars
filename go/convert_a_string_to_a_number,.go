// 8 kyu kata

package kata

import "strconv"

func StringToNumber(str string) int {
  ret, _ := strconv.Atoi(str)
  return ret
}

// I learned about the stl strconv, and Atoi
// which returns an int and an error state
// in the event of any conversion issues