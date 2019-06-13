#include <bits/stdc++.h>
using namespace std;

int main(){
 int n, result=0;
 int a, b;
 cin >> n;

 for(int i=0;i<n;i++){
 	cin >> a >> b;
   	result += b-a+1;
 }
 cout << result << endl;
 
}