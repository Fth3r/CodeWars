// Solving the 6 kyu kata The Mexican Wave

func wave(_ y: String) -> [String] {
  var ret = [String]()
  
  for i in y.indices {
    if !(y[i].isWhitespace) {
      var mut = y
      mut.replaceSubrange(i...i, with: y[i].uppercased())
      ret.append(mut)
    }
  }
  return ret
}


// Second kata with Swift, could have shortened it up some like this 

func wave(_ y: String) -> [String] {
  var wave = [String]()
  for i in y.indices {
    if !y[i].isWhitespace {
      wave.append(y[..<i] + y[i].uppercased() + y[y.index(after: i)...])
    }
  }
  return wave
}

// And then of course there's the wizard answer...

func wave(_ y: String) -> [String] {
  return Array(y).enumerated().compactMap { $1.isWhitespace ? nil : y.prefix($0) + $1.uppercased() + y.dropFirst($0 + 1)}
}

