#include <bits/stdc++.h>
using namespace std;

int main(){
  int n, p;
  string s;
  cin >> n;
  
  tuple<string, int, int>r[110];
  for(int i=0;i<n;i++){  
    cin >> s >> p;
    r[i]=make_tuple(s,-p,i+1);
  }
   for(int i=0;i<n;i++){  
	sort(r, r+n);
    cout << get<2>(r[i]) << endl;
  }
}