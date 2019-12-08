#include <iostream>
#include <cassert>
#include <vector>

using std::vector;

int binary_search(const vector<int> &a, int x, int left, int right) {
  //write your code here
  if(right < left){
    return -1;
  }
  int idx = (left + right) / 2;
  if(a[idx] == x) return idx;
  
  if(a[idx] > x) right = idx-1;
  else left = idx + 1;
  return binary_search(a, x, left, right);

}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    std::cout << binary_search(a, b[i], 0, a.size());
    if(i != m-1) std::cout<< ' ';
  }
  std::cout<<std::endl;
}
