// 6 kyu kata

package kata

// here the return type (outs []int) creates the array of ints
// and tells the function to return outs. Saves a line for the declaration
func Parse(data string) (outs []int) {
  v := 0
  for _, val := range data {
    switch val {
      case 'i': v++
      case 'd': v--
      case 's': v *= v
      case 'o': outs = append(outs, v)
    }
  }
  return // because I used (outs []int) above it knows what to return
}

// My first 6 kyu golang kata, woo! 
