#include <iostream>
#include <vector>

using std::vector;

vector<int> optimal_summands(int n) {
  vector<int> summands;
  //write your code here
  int remaining = n;
  for(int i=1; i<=n; i++){
    if(remaining >= i) {
      summands.push_back(i);
      remaining -= i;
    }else{
      summands[(int)summands.size()-1] += remaining;
      break;
    }
  }

  return summands;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
  std::cout<<std::endl;
}
