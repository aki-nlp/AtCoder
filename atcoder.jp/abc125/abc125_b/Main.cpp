#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin >> n;
  int x=0,v[50],c[50];
  for(int i=0;i<n;i++){
    cin >> v[i];
  }
  for(int i=0;i<n;i++){
    cin >> c[i];
  }
  for(int i=0;i<n;i++){
    if(v[i]-c[i]>0)x+=v[i]-c[i];
  }
  cout << x << endl;
}