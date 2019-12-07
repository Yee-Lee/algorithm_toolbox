#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  int start, end;
};

bool compareEndPoint(Segment s1, Segment s2){
  if(s1.end > s2.end) return false;
  return true;
}

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  //write your code here

  //sort the segments by the end points
  sort(segments.begin(), segments.end(), compareEndPoint);

  //The first point is the end of the first segments.
  int the_point = segments[0].end;
  points.push_back(the_point);

  for(size_t i=1; i<segments.size(); i++){
    if(segments[i].start > the_point){
      //cannot cover, have to set it as the new point.
      the_point = segments[i].end;
      points.push_back(the_point);
    }
  }
  
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
