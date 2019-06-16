#include<bits/stdc++.h>
using namespace std;

int main(){
  int W, H, x, y;
  cin >> W >> H >> x >> y;
  printf("%f %d", double(W)*double(H)/2, x+x==W&&y+y==H);
}
