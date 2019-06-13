#include <bits/stdc++.h>
using namespace std;

int main(){
 int n, k;
 int keiji=1;
 cin >> n >> k;
 
 for(int i=0;i<n;i++){
   if(keiji*2<keiji+k) keiji*=2;
   else keiji+=k;
 }
 
  cout << keiji << endl;
}