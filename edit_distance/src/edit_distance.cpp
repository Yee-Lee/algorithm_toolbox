#include <iostream>
#include <string>
#include <algorithm>

using std::string;
using std::min;

/*
     colnum = str1.size()+1
**D    j [0] [1] [2] [3]
     * 0  1   2   3   4
 i   0
[0]  1
[1]  2  

rownum = str2.size()+1
*/

int edit_distance(const string &str1, const string &str2) {
  //write your code here
  int colnum = str1.size()+1;
  int rownum = str2.size()+1;

  int **D;
  D = new int*[rownum];
  for(int i=0; i<rownum; i++){
    D[i] = new int[rownum]; 
    for(int j=0; j<colnum; j++)
      if(i==0) D[0][j] = j;
      else if(j==0) D[i][0] = i;
      else D[i][j] = 0;
  }

  for(int i=1; i<rownum; i++){
    for(int j=1; j<colnum; j++){
      int d1,d2,d3,d4;
      d1 = D[i][j-1] + 1; //Insert 
      d2 = D[i-1][j] + 1; //Delete
      d3 = D[i-1][j-1] +1;//Replace
      d4 = D[i-1][j-1];   //Do nothing, only in matched

      int minD = 0;
      minD = min(d1, d2);
      //If the current chars are matched
      if(str1[j-1] == str2[i-1]){
        minD = min(minD, d4);
      }else{
        minD = min(minD, d3);
      }
      D[i][j] = minD;
    }
  }
  /*
  for(int i=0; i<rownum; i++){
    for(int j=0; j<colnum; j++)
      std::cout<<D[i][j]<<" ";
    std::cout<<std::endl;
  }*/
  int ret = D[rownum-1][colnum-1]; 
  for(int i=0; i<rownum; i++)
    delete [] D[i];
  delete [] D;
  
  return ret ;
}

int main() {
  string str1;
  string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}
