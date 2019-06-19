#include <bits/stdc++.h>
using namespace std;

int main(){
  int r, d, x;
  cin >> r >> d >> x;
  
  int a[11];
  a[0]=x;
  for(int i=0; i<10; i++){
  	a[i+1]=r*a[i]-d;
    cout << a[i+1] << endl;
  }
  
}