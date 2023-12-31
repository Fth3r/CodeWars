// 8 kyu kata
// It's actually called I love you, a little, a lot, passionately ... not at all

package kata

func HowMuchILoveYou(i int) (ret string) {
  switch i % 6 {
    case 1:ret = "I love you"
    case 2:ret = "a little"
    case 3:ret = "a lot"
    case 4:ret = "passionately"
    case 5:ret = "madly"
    case 0:ret = "not at all"
  }
  
  return
}

// I was able to utilize the switch statement format I saw 
// after submitting my solution to the Qaurter of the year kata
// which makes it much more readable that doing this with 
// a bunch of if/else if statements

// Here I thought I was doing pretty well
// and then I saw this in the solutions to this kata...

package kata

func HowMuchILoveYou(i int) string {
    return []string{"I love you","a little","a lot","passionately","madly","not at all"}[(i-1) % 6]
}

// How very simple and elegant. Well Done.