#include <iostream>

using namespace std;

int main(void){

  int A, B;
  cin >> A >> B;

  int m, n, r;
  m = n = r = 0;
  if( A > B){
    m = A;
    n = B;
  }else{
    m = B;
    n = A;
  }

  do {
    r = m % n;
    if(r == 0)
      break;
    m = n;
    n = r;
  }while(true);

  cout << n << endl;
  return 0;
}
