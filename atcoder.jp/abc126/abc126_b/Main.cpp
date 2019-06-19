#include <bits/stdc++.h>
using namespace std;

int main(){
  int s;
  cin >> s;
  int a, b, c, d;
  a=s/100;
  b=s%100;

  if((a==0||a>12)&&b<13&&b!=0)
   cout << "YYMM" << endl;
  else if((b==0||b>12)&&a<13&&a!=0)
    cout << "MMYY" << endl;
  else if((a!=0&&a<13)||(b!=0&&b<13))
    cout << "AMBIGUOUS" << endl;
  else
    cout << "NA" << endl;
}