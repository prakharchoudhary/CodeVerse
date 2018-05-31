#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void printParens(int i, int j, int n, int *s, char &name)
{
    if (i == j)
    {
        cout << name++;
        return;
    }
 
    cout << "(";

    printParens(i, *((s+i*n)+j), n,
                     s, name);

    printParens(*((s+i*n)+j) + 1, j,
                     n, s, name);
    cout << ")";
}

void matrixChainOrder(int *p, int n){
	int i, j, k, l, q;
	int m[n][n];
	int s[n][n];

	for(i=1; i<n; i++){
		m[i][i] = 0;
	}

	for(l=2; l<n; l++){
		for(i=1; i<n-l+1; i++){
			j = i+l-1;
			m[i][j] = INT_MAX;
			for(k=i; k<=j-1; k++){
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
				if(q<m[i][j]){
					m[i][j] = q;
					s[i][j] = k;
				}
			}
		}
	}

	char name = 'A';

    cout << "Optimal Parenthesization is : ";
    printParens(1, n-1, n, (int *)s, name);
    cout << "\nOptimal Cost is : " << m[1][n-1]<<endl;
}

int main()
{
    int arr[] = {40, 20, 30, 10, 30};
    int n = sizeof(arr)/sizeof(arr[0]);
    matrixChainOrder(arr, n);
    return 0;
}