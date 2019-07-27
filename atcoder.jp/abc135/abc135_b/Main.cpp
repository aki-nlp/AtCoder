#include<bits/stdc++.h>
using namespace std;

int main(){
 int n ,a;
 int flag=0;
 cin >> n;
 for(int i=0;i<n;i++){
 	cin >> a;
   	if(a!=i+1) flag++;
 }
  
 if(flag==0||flag==2){
   cout << "YES" << endl;
 }else{
   cout << "NO" << endl;
 }
  
}