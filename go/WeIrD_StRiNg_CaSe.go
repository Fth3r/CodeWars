// 6 kyu kata

package kata

import "strings"

func toWeirdCase(str string) string {
  s := []string{}
  ret := ""
  for i,j := 0,0; i < len(str); i++ {
    if string(str[i]) == " " { 
      s = append(s, string(str[i]))
      j = 0
      continue
    } else if j % 2 == 0 {
      s = append(s, strings.ToUpper(string(str[i])))
      j++
    } else {
      s = append(s, strings.ToLower(string(str[i])))
      j++
    }
  }
  
  return strings.Join(s, ret)
}

// in retrospect I didn't need to use an intermediate slice of strings, I could have 
// used += to add to ret instead of append to s. This would have saved me a line and the
// time used for joining the slice into a string in the return statement.
//
// Apparently, the more idiomatic way to do it would have been to use the "unicode" library
// and append the runes as I went, turning it into a string in the return. This library
// also has a .ToUpper() method that would have been useful...
// Live and learn, I guess! 
