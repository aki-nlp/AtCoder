#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,a,b;
  cin >> n;
  pair<int, int>w[n];
  for(int i=0;i<n;i++){
  	cin >> a >> b;
    w[i] =make_pair(b, a);
  }
  sort(w, w+n);
  
  int sum=0;
  bool flag=true;
  for(int i=0;i<n;i++){
    sum+=w[i].second;
  	if(sum>w[i].first) flag=false;
  }
  
  if(flag) cout << "Yes" <<endl;
  else cout << "No" <<endl;
}