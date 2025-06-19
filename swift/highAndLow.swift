// Solving the 7 kyu kata high and low

func highAndLow(_ numbers: String) -> String {
  let arr = numbers.split(separator: " ")
  var nums = [Int]()
  for i in arr { nums.append(Int(i)!) }
  return "\(nums.max()!) \(nums.min()!)"
}

// I didn't know about compactMap, which would have simplified it for me as such

func highAndLow(_ numbers: String) -> String {
    let numbers = numbers.split(separator: " ").compactMap { Int($0) }
    return "\(numbers.max()!) \(numbers.min()!)"
}

// But at the savings of only two lines I guess the longer form isn't that bad
