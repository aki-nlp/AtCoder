#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,d;
  int result=0,s;
  int x[n+10][d+10];
  cin >> n >> d;
  for(int i=0;i<n;i++){
    for(int j=0;j<d;j++){
      cin >> x[i][j];
    }
  }
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      s=0;
      for(int k=0;k<d;k++){
        s+= pow(x[i][k]-x[j][k],2);
      }
      //cout<<sqrt(s)<<endl;
      double d=sqrt(s);
      if(d==int(d))result++;
    }
  }
  cout << result << endl;
}