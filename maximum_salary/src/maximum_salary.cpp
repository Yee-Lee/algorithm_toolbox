#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

bool compareNumber(string s1, string s2){
  int len1 = s1.length();
  int len2 = s2.length();
  if (len1 == len2){
    return (stoi(s1) - stoi(s2)) >= 0;
  }
  else if (len1 > len2){
    int dif = len1 - len2;
    char last = s2.at(len2-1);
    s2.append(dif, last);
    return (stoi(s1) - stoi(s2)) >= 0;
  }
  else {
    int dif = len2 - len1;
    char last = s1.at(len1-1);
    s1.append(dif, last);
    return (stoi(s1) - stoi(s2)) >= 0;
  }

}

string largest_number(vector<string> a) {
  //write your code here

  sort(a.begin(), a.end(), compareNumber);

  std::stringstream ret;
  for (size_t i = 0; i < a.size(); i++) {
    ret << a[i];
  }
  string result;
  ret >> result;
  return result;
}

int main() {
  int n;
  std::cin >> n;
  vector<string> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::cout << largest_number(a)<<std::endl;
}
