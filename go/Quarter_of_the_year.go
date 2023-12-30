// 8 kyu kata

package kata

func QuarterOf(month int) int {
  quarters := map[int]int {
    // month: quarter
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 3,
    10: 4,
    11: 4,
    12: 4,
  }
  
  for key, value := range quarters {
    if key == month {
      return value
    }
  }
  return 0 // should never get here, but it needed a final return?
  // IDK I'm new here
}

// Like I thought, this was a silly way of doing it but it worked
// a better way would have been with a switch statement like this

func QuarterOf(month int) (result int) {
  
	switch month{
	  case 1,2,3:result = 1
	  case 4,5,6:result = 2
	  case 7,8,9:result = 3
	  case 10,11,12:result = 4
	}
	return
  }

  // or if I had been thinking algorithmically...

  func QuarterOf(month int) int {
	return (month + 2) / 3
  }