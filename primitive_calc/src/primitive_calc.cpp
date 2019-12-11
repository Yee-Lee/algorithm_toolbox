#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

vector<int> optimal_sequence(int n) {
  vector<int> sequence;
  vector<int> rec;
  rec.push_back(0); //0
  for(int i=1; i<n+1; i++){
    int min = rec.at(i-1);
    if(i%2==0) min = rec.at(i/2) < min ? rec.at(i/2) : min;
    if(i%3==0) min = rec.at(i/3) < min ? rec.at(i/3) : min;
    rec.push_back(min+1);
  }
  int s = rec[n];
  //trace back
  while(n>0)
  {
    if(n%3==0 && rec[n/3] == s-1){
    sequence.push_back(n);
      n = n/3;
    }else if(n%2 == 0 && rec[n/2]==s-1){
    sequence.push_back(n);
      n = n/2;
    }
    else
    {
    sequence.push_back(n);
      n = n-1;
    }
    s--;
  }
  reverse(sequence.begin(), sequence.end());
  return sequence;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> sequence = optimal_sequence(n);
  std::cout << sequence.size() - 1 << std::endl;
  for (size_t i = 0; i < sequence.size(); ++i) {
    std::cout << sequence[i];
    if(i!=sequence.size()-1) std::cout<< " ";
  }
  std::cout<<std::endl;
}
