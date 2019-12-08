#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

int partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      j++;
      swap(a[i], a[j]);
    }
  }
  swap(a[l], a[j]);
  return j;
}

//write down your code 
int partition3(vector<int> &a, int l, int r, int &lm, int &rm){
  int x = a[l];

  vector<int> am, al, ar;
  for (int i = l+1; i <= r; i++) {
    if (a[i] < x) al.push_back(a[i]);
    else if (a[i] == x) am.push_back(a[i]);
    else ar.push_back(a[i]); 
  }
  am.push_back(x);
  
  lm = l + (int)al.size();
  rm = lm + (int)am.size();
  
  al.insert(al.end(), am.begin(), am.end());
  al.insert(al.end(), ar.begin(), ar.end());
  al.insert(al.begin(), a.begin(), a.begin()+l);
  al.insert(al.end(), a.begin()+r+1, a.end());
  a.clear();
  a.assign(al.begin(), al.end());
  // std::cout<<std::endl;
  //for (size_t i = 0; i < a.size(); ++i) {
  //  std::cout << a[i] << ' ';
 // }
 // std::cout<<std::endl;

  return 0;
}


void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  //int m = partition2(a, l, r);

  int lm, rm;
  //std::cout<<a[l]<<":";
  partition3(a, l, r, lm, rm);
  //std::cout<<l<<" "<<lm<<" "<<rm<<" "<<r<<std::endl;

  randomized_quick_sort(a, l, lm - 1);
  randomized_quick_sort(a, rm, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i];
    if(i != a.size()-1) std::cout << ' ';
  }
  std::cout<<std::endl;
}
