#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long int N,M,p,q,inc,max=0,x=0,i;
    cin>>N>>M;
    long int *arr = new long int[N+1]();
    
    for(i=0; i<M; i++)
    {
        cin>>p>>q>>inc;
        arr[p] += inc;
        if(q+1<=N){arr[q+1] -= inc;}
    }
    
    for(i=1; i<=N; i++)
    {
        x = x+arr[i];
        if(max<x)
            max=x;
    }
    cout<<max;
    return 0;
}