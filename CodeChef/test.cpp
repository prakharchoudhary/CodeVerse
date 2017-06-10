#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long int arr[5], min;
    int i, j;
    for(i=0; i<5; i++)
    {
        cin>>arr[i];
    }

    for(i=0; i<5; i++)
    {
        for(j=i; j<5; j++)
        {
            if(arr[i]>arr[j]) swap(arr[i], arr[j]);  
        }
    }
    
    for(i=0; i<5; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
    return 0;
}