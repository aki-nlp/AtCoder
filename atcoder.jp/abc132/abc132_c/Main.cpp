#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,r=0; 
  cin >> n;
  vector<int> a(n);
  for(int i=0;i<n;i++){
    cin>>a[i];
  }  
  sort(a.begin(),a.end());
  
  cout<<a[n/2]-a[n/2-1]<<endl;
}