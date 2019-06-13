#include <bits/stdc++.h>
using namespace std;

int main(){
 int x, fx;
 cin >> x;
 int n = x;
  
 while(x>0){
   fx += x%10;
   x /= 10;
 }
  
 if(n%fx==0) cout << "Yes" << endl;
 else cout << "No" << endl;
}