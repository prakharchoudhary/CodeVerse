#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> v[100005];

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, q, type, x, y;
    cin>>n>>q;
    int lastans = 0;
    while(q--)
    {
        cin>>type>>x>>y;
        if(type == 1)
        {
            v[(lastans^x)%n].push_back(y);
        }
        else
        {
            int pos = (lastans^x)%n;
            int idx = y%((int)v[pos].size());
            lastans = v[pos][idx];
            cout<<lastans<<endl;
        }
    }
    return 0;
}