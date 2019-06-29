#include <bits/stdc++.h>
using namespace std;

int main(){
  string n; 
  int a[1000]={};
  cin >> n;
  bool flag=true;
  for(int i=0;i<4;i++){
     a[(int)n[i]]++;
    //cout<<a[(int)n[i]]<<endl;
  }
  for(int i=0;i<1000;i++){
    if(a[i]!=0&&a[i]!=2){
       //cout<<a[i]<<endl;
       flag=false;
       break;
    }
  }
    if(flag)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
  
}