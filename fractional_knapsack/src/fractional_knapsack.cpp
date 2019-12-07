#include <iostream>
#include <vector>

using std::vector;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;

  // write your code here
  int n = weights.size();
  
  vector<float> lefts;
  lefts.assign(weights.begin(), weights.end());

  float available = (float)capacity;
  int best_item = 0;
  float best_cp = 0;
  while(available > 0){
    best_item = 0;
    best_cp = 0;
    for(int i=0; i<n; i++){
      if(lefts[i] > 0){
        if(((float)values[i]/weights[i]) > best_cp){
          best_cp = (float)values[i]/weights[i];
          best_item = i;
        }
      }
    }
    //std::cout<<"best item:"<<best_item;
    float taken_weights = (available - lefts[best_item]) >= 0? lefts[best_item] : available;
    //std::cout<<"taken:"<<taken_weights;
    value += taken_weights * ((float)values[best_item]/weights[best_item]);
    available -= taken_weights;
    lefts[best_item] -= taken_weights;
  }

  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
