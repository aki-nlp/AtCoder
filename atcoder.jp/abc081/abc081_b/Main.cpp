#include <bits/stdc++.h>
using namespace std;

int main(){
 int N, result=0,flag=true;
 cin >> N;
 int A[N];
  
 for(int i=0;i<N;i++){
   	cin >> A[i];
 }
  
 while(flag){
   for(int i=0;i<N;i++){
   	if(A[i]%2==1) { flag=false; break; }
    A[i] /= 2;
   }
   if(flag) result++;
 }
 
  cout << result << endl;
}