#include <iostream>

using namespace std;
int main()
{
    int T, G, I, Q;
    long int N, out;
    cin>>T;
    while(T--)
    {
        cin>>G;
        while(G--)
        {
            cin>>I>>N>>Q;
            out = N/2;
            if(I != Q && N%2 != 0)
                out = out + 1;
            cout<<out<<endl;
        }
    }
    return 0;
}