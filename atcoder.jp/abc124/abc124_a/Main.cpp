#include<bits/stdc++.h>
using namespace std;

int main(){
  int A, B, T, result=0;
  cin >> A >> B;

  for(int i=0;i<2;i++){
    if(A>B){
  	  result += A--;
    } else {
      result += B--;
    }
  }
  cout << result << endl;
}