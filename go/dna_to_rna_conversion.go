package kata

func DNAtoRNA(dna string) string {
  r := []rune(dna)
  for i := 0; i < len(r); i++ {
    if r[i] == 'T' {
      r[i] = 'U'
    }
  }
  return string(r)
}

// golang seems to use what python calls the "walrus operator"
// to declare and assign variables at the same time. Interesting.

// apparently I could have done this much easier by using the 
// strings stl like this

package kata

import "strings"

func DNAtoRNA(dna string) string {
	return strings.ReplaceAll(dna, "T", "U")
}

// but as I have said before, I'm just picking up golang
// so that's a good learning experience for me! 