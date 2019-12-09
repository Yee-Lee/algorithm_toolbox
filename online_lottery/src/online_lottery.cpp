#include <iostream>
#include <vector>

#include <algorithm>

using std::vector;

struct aux{
  int pos;
  int sign;
};

bool compareAux(aux a1, aux a2){
  return (a1.pos >= a2.pos)? false : true;
}

vector<int> fast_count_segments(vector<int> starts, vector<int> ends, vector<int> points) {
  vector<int> cnt;
  //write your code here
  
  //build a record table for +1 as start_point and -1 as end_point

  vector<aux> rec;
  for(auto p : starts){
    aux s = {p, 1};
    rec.push_back(s);
  }
  for(auto p : ends){
    aux e = {p, -1};
    rec.push_back(e);
  }
  std::sort(rec.begin(), rec.end(), compareAux);
  
  int acc = 0;
  for(auto &a : rec){
    acc += a.sign;
    a.sign = acc;
  }

  /* Find the nearest last aux point, check its sign. That is the number of covering
     For example:
     --------- { --- {----}-{-----}------}---{-----}----------
     ----------1-----2----1-2-----1------0---1-----0---------
     ------------------*-------------------*------------------
                      (2)                 (0)
  */

  for(auto p : points){
    //corner case
    if(p < rec[0].pos || p > rec[rec.size()-1].pos)
      cnt.push_back(0);
    else{    
      int left = 0;
      int right = rec.size();
      int idx = (left+right)/2;
      while(right-1>left && rec[idx].pos!=p){
        if(rec[idx].pos > p) right = idx;
        else left = idx;
        idx = (left + right)/2;
      }
      //idx is the nearest left point;
      cnt.push_back(rec[idx].sign);
    }
  }
   
  return cnt;
}

vector<int> naive_count_segments(vector<int> starts, vector<int> ends, vector<int> points) {
  vector<int> cnt(points.size());
  for (size_t i = 0; i < points.size(); i++) {
    for (size_t j = 0; j < starts.size(); j++) {
      cnt[i] += starts[j] <= points[i] && points[i] <= ends[j];
    }
  }
  return cnt;
}

int main() {
  int n, m;
  std::cin >> n >> m;
  vector<int> starts(n), ends(n);
  for (size_t i = 0; i < starts.size(); i++) {
    std::cin >> starts[i] >> ends[i];
  }
  vector<int> points(m);
  for (size_t i = 0; i < points.size(); i++) {
    std::cin >> points[i];
  }
  //use fast_count_segments
  //vector<int> cnt = naive_count_segments(starts, ends, points);
  vector<int> cnt = fast_count_segments(starts, ends, points);
  for (size_t i = 0; i < cnt.size(); i++) {
    std::cout << cnt[i] ;
    if(i != cnt.size()-1) std::cout<< ' ';
  }
  std::cout << std::endl;
}
