// 6 kyu kata

package kata

import "strings"

func CamelCase(s string) (ret string) {
  if s == "" { return }
  t := strings.TrimSpace(s)
  ret += strings.ToUpper(string(t[0]))
  for i := 1; i < len(t); i++ {
    if string(t[i]) == " " {
      ret += strings.ToUpper(string(t[i+1]))
      i++
    } else { ret += string(t[i]) }
  }
  return
}

// as usually happens, I took the long way when I could have 
// done this much much more quickly, like this ...

func CamelCase(s string) string {
	return strings.Replace(strings.Title(s)," ","",-1)
}
