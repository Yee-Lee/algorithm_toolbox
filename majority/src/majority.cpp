#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

/*
*  Find out the majority from the left side and the right side.
*  Vote for the final majority.
*  Test the final majority is over the half of the whole sequence.
*
*/

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return a[left];
  if (left + 1 == right) return a[left];
  //write your code here

  int half = (left+right)/2;
  int majority_left = get_majority_element(a, left, half);
  int majority_right = get_majority_element(a, half+1, right);
  
  int vote_left = 0;
  int vote_right= 0;
  for(int i=left; i < right; i++){
    if(a[i] == majority_left) vote_left++;
    if(a[i] == majority_right) vote_right++;
  }
  int m = (vote_left > vote_right)? majority_left : majority_right;

  return m;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  int vote = 0;
  int m = get_majority_element(a, 0, a.size());
  int len = a.size();
  for(int i=0; i<len; i++){
    if(a[i] == m) vote++;
  }
  int ret = ( vote > len/2 )? m : -1;
  std::cout <<  ret << '\n';
}
