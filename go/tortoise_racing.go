// 6 kyu kata

package kata

import ("fmt")

func Race(v1, v2, g int) [3]int {
  if v2 < v1 { return [3]int{-1,-1,-1} }

  r := v2 - v1
  t := float64(g)/float64(r)
  
  h := int(t)
  m := int(((t - float64(h)) * 60) + .0000000001)
  fmt.Print("minutes: ", (t - float64(h)) * 60)
  s := int((((t - float64(h)) * 60) - float64(m)) * 60)
  return [3]int{h,m,s}
}

// This gave me some trouble for a while. I have a rounding error
// somehere that only shows up if the remainder of m or s is
// 0.99999999999... the other cases all rounded fine, so I had to
// add 0.00000000001 to round that case up but not affect the others
// that were working
//
// alternately, a much more simple and elegant solution than my 
// somewhat hamfisted approach would have been

package kata

func Race(v1, v2, g int) [3]int {
  if v1 >= v2 {
    return [3]int{-1, -1, -1}
  }
  s := g * 3600 / (v2 - v1)
  return [3]int{s / 3600, (s / 60) % 60, s % 60} 
}

// from user jbstjohn. Well done, so much simpler and cleaner. 
