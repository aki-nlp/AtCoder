#include <bits/stdc++.h>
using namespace std;

int main(){
  int n, h, now=-1, x=0;
  cin >> n;
  for(int i=0;i<n;i++){
    cin >> h;
    if(h>=now){
      now=h;
      x++; 
    }
  }
  cout << x << endl;
}