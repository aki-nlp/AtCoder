#include <bits/stdc++.h>
using namespace std;

int main(){
 int n, k, x, result=0;
 cin >> n >> k;
 
 for(int i=0;i<n;i++){
 	cin >> x;
   	if(x<k-x) result+=x*2;
    else result+=(k-x)*2;
 }
 
  cout << result << endl;
}