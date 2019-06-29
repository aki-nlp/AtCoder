#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,r=0; 
  int a[30]={};
  cin >> n;
  for(int i=0;i<n;i++){
    cin>>a[i];
  }  

  for(int i=1;i+1<n;i++){
    if((a[i-1]<a[i]&&a[i]<a[i+1])
       ||(a[i-1]>a[i]&&a[i]>a[i+1]))r++;
  }
  cout<<r<<endl;
}