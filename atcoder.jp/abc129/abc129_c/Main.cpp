#include <bits/stdc++.h>
using namespace std;
const long long mod=1e9+7;


int main(){
  int N, M;
  cin >> N >> M;
  
  vector<int>A(N+1, 1);
  for(int i=0;i<M;i++){
    int a;
    cin >> a;
    A[a]=0;
  }
  
  vector<long long int>p(N+1);
  p[0]=1;
  for(int now=0;now<N;now++){
    for(int next=now+1;next<=min(N,now+2);next++){
      if(A[next]){
        p[next]+=p[now];
		p[next]%=mod;
      }
    }
  }
   
  cout<<p[N]<<endl;

}