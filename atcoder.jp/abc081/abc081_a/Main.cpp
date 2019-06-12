#include <bits/stdc++.h>
using namespace std;

int main(){
  	int s,s1,s2,s3;
	cin >> s;
  	s1 = s/100;
  	s2 = (s%100)/10;
    s3 = (s%100)%10;
  	cout << s1+s2+s3 << endl;
}