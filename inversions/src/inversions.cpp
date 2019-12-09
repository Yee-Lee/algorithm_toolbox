#include <iostream>
#include <vector>

using std::vector;


/*
*   Use mergesort to count the number of inversions.
*   An inversion occurs at a place that an element in the right array is inserted into the merged array before the elements in the left array.
*   Hence, when such an insertion occurs, the inversions are the number of elements remaining in the left array.
*
*   vector a is the original array. vector b is an auxiliary array.
*/

long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right) {
  long long number_of_inversions = 0;
  if (right <= left + 1) return number_of_inversions;
  size_t ave = left + (right - left) / 2;
  number_of_inversions += get_number_of_inversions(a, b, left, ave);
  number_of_inversions += get_number_of_inversions(a, b, ave, right);
  //write your code here

  //copy the segement to the auxiliary array b.
  for(size_t i=0; i<right-left; i++){
    b[left+i] = a[left+i];
  }
  //merge [left, ave] and [ave, right]
  size_t l = left; // the index of left and right arrays.
  size_t r = ave;
  for(size_t i=0; i<right-left; i++){
    if(l==ave){
      a[left+i] = b[r];
      r++;
    }
    else if(r==right){
      a[left+i] = b[l];
      l++;
    }
    else{
      if(b[l] <= b[r]){ // use an element in the left array.
        a[left+i] = b[l];
        l++;
      }else 
      {// An inversion occurs, count the number of elements left in the left array.
        a[left+i] = b[r];
        r++;
        number_of_inversions += (ave-l);
      } 
    }
  }
  return number_of_inversions;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  vector<int> b(a.size());
  std::cout << get_number_of_inversions(a, b, 0, a.size()) << '\n';
}
