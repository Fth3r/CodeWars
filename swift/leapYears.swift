func isLeapYear(_ year: Int) -> Bool {
  if year % 4 == 0 && year % 100 != 0 { return true }
  if year % 400 == 0 { return true }
  
  return false
}


// That was what I came to, but this is my first kata using swift as I'm trying to learn the language.
// The more /swifty/ way to do it would probably have been as follows

func isLeapYear(_ year: Int) -> Bool {
  (year.isMultiple(of: 400)) || (year.isMultiple(of: 4) && !year.isMultiple(of: 100))
}

// But I didn't know that method existed in the STL! Live and learn...
