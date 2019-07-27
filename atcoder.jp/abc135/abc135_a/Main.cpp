#include<bits/stdc++.h>
using namespace std;

int main(){
 int a,b;
 cin >> a >> b;
 if((b-a)%2!=0){
   cout << "IMPOSSIBLE" << endl;
 }else{
   cout << abs(a+(b-a)/2) << endl;
 }
  
}