#include <bits/stdc++.h>
using namespace std;

int main(){
 int A, B, result=0;
 int a, b, d, e; //abcde
 cin >> A >> B;
 
 
 for(int i=A;i<=B;i++){
   	a = (i/10000%10);
    b = (i/1000%10);
    d = (i/10%10);
    e = i%10;
   	if(a==e&&b==d) result++;
 }
 
  cout << result << endl;
}