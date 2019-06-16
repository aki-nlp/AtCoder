#include <bits/stdc++.h>
using namespace std;

int main(){
 int N, X;
 cin >> N >> X;
 int L[N], D[N+1]={0};
 for(int i=0;i<N;i++){
  cin >> L[i] ;
 }
 int count=1;
 for(int i=1;i<N+1;i++){
   D[i]=D[i-1]+L[i-1];
   if(D[i]<=X) count++;
 }
  
 cout << count << endl;
}