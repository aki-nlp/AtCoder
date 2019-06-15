#include<bits/stdc++.h>
using namespace std;

int main(){
  int A, B, T, result=0;
  string S;
  cin >> A >> B >> T;
  int j=1;
  for(int i=0;i<T+1;i++){
    if(i!=0&&i%(A*j)==0){
  	  result += B;
      j++;
    }
  }
  cout << result << endl;
}