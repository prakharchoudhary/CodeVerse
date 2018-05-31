#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
       int i, N;
       cin>>N;
       int songs[1000];
       for(i=0;i<N;i++)
       {
           cin>>songs[i];
       }
       int k;cin>>k;
       int temp=songs[k-1];
       sort(songs,songs+N);
       for(i=0;i<N;i++)
       {
           if(songs[i]==temp)
           cout<<i+1<<endl;
       }
 
    }
    return 0;
}