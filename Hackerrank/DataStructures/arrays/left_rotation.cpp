#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int arr[100000], result[100000], i, index;
    int s, r;
    cin>>s>>r;
    for(i=0; i<s; i++)
    {
        cin>>arr[i];     
    }
    
    if(r%s == 0)
    {
        for(i=0; i<s; i++)
        {
        cout<<arr[i];     
        }
        return 0;
    }
    
    r = r%s;
    
    for(i=0; i<s; i++)
    {
        index = s+i-r;
        if(index>=s)
            index = index-s;
        result[index] = arr[i];   
    }
    
    for(i=0; i<s; i++)
    {
        cout<<result[i]<<" ";     
    }
    return 0;
}
