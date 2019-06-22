#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,l, sum=0, t;
  cin >> n >> l;
  pair<int, int>a[n];
  for(int i=0;i<n;i++){
    if(l+i>0) t=1;
    else t=-1;
    a[i]=make_pair(l+i,t);
    sum+=l+i;
    if(l+i<0)a[i].first*=-1;
  }
  sort(a,a+n);
  cout <<sum-a[0].first*a[0].second<<endl;
    
}