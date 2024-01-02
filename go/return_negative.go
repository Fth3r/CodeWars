// 8 kyu kata

package kata

func MakeNegative(x int) int {
  switch x < 0{
    case true: return x
    case false: return 0-x
  }
  return 0
}

// This is what I submitted. It could have been simpler to do ...

func MakeNegative(x int) int {
  if x <= O { return x }
  return -x
}
