#include <iostream>


// Dyanmic programming 
// Use 1, 3, 4 for money change
int get_change(int m) {
  //write your code here

  int *num_coins = new int[m+1];
  num_coins[0] = 0;
  for(int i=1; i<m+1; i++){
    int min = num_coins[i-1];
    if(i>=3)
      min = num_coins[i-3] < min ? num_coins[i-3] : min;
    if(i>=4)
      min = num_coins[i-4] < min ? num_coins[i-4] : min;
    num_coins[i] = min + 1;
    
    //std::cout << i << std::endl;
    //std::cout << min << std::endl;
  }
  int ret = num_coins[m];
  delete num_coins;
  return ret;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
