// 6 kyu kata
int persistence(long long n) {
  if(n / 10 != 0) { 		
    int r = n % 10; 		
    while((n /= 10) != 0) { r *= n % 10; }
    return 1 + persistence(r); 	
  }
  return 0; 
}
