#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::max;

/*
  The value of items is same as its weight.
 
      Capacity  0 1 2 3 4...W
items  -------------------------------
 idx  |
  0   |  values of the whole knapsack
  1   |
  2   |
  3   |
(The items under consideration. Taken or not taken cannot be seen in this table.)
*/

int optimal_weight(int W, const vector<int> &w, vector<int> &V) {
  //write your code here
  int **D;
  D = new int* [w.size()];
  for(int i=0; i<(int)w.size(); i++){
    D[i] = new int[W+1];
    D[i][0] = 0; // initialization
  }

  for(int i=0; i<(int)w.size(); i++){
    int w_i = w[i];
    int v_i = V[i];
    for(int c=1; c<W+1; c++){
      int v = 0;
      if(c >= w_i){
        if(i>0){
          v = max(D[i-1][c], D[i-1][c-w_i]+v_i);
        }else{
          v = v_i;
        }
      }else{ // must not pick i up
        v = (i>0)? D[i-1][c]: 0;
      }
      D[i][c] = v;
    }
  }

/*
  for(int i=0; i<(int)w.size(); i++){
    for(int j=0; j<W+1; j++)
      std::cout<<D[i][j]<<" ";
    std::cout<<std::endl;
  }
*/
  
  int ret = D[(int)w.size()-1][W];
  for(int i =0; i<(int)w.size(); i++)
    delete [] D[i];
  delete [] D;

  return ret;
}

int main() {
  int n, W;
  std::cin >> W >> n;
  vector<int> w(n);
  for (int i = 0; i < n; i++) {
    std::cin >> w[i];
  }
  vector<int> V(n);
  for(int i=0 ; i<n; i++)
  std::cin >> V[i]; 
  std::cout << optimal_weight(W, w, V) << '\n';
}
