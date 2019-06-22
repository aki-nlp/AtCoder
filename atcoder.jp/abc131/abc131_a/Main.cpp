#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,a,b,c,d;

  cin >> n;
  a=n/1000;
  b=n/100%10;
  c=n/10%10;
  d=n%10;

  if(a-b==0|b-c==0|c-d==0)
    cout << "Bad" << endl;
  else
  	cout << "Good" << endl;

    
}