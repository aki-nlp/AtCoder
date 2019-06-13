#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  int W[100],d;
  int sum=0,sum2=0;
  
  for(int i=0;i<N;i++){
    cin >> W[i];
    sum+=W[i];
  }
  d = sum;
  
  for(int i=0;i<N;i++){
    sum2+=W[i];
    
    d = min(d, abs(sum-sum2*2));
  }
  
  cout<<d<<endl;

}