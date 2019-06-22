#include <bits/stdc++.h>
using namespace std;

long long int gcd(long long int a, long long int b) {
  if (b==0)
    return a;
  return gcd(b, a%b);
}

unsigned long long int lcm(long long int a, long long int b) {
  return a*b/gcd(a, b);
}

int main(){
  long long int a, b;
  int c, d;
  unsigned long long int e;
  long long int c1=0, c2=0, c3=0, c4;
  long long int d1=0, d2=0, d3=0, d4;
  cin >> a >> b >> c >> d;
  long long int sum=b-a+1;
  e=lcm(c, d);
  
  c1=b/c;
  c2=b/d;
  c3=b/e;
  c4=b-(c1+c2-c3);
 
  d1=(a-1)/c;
  d2=(a-1)/d;
  d3=(a-1)/e;
  d4=(a-1)-(d1+d2-d3);  
  
  cout <<c4-d4<< endl;
}