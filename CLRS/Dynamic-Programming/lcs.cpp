#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

void lcs( char *X, char *Y, int m, int n )
{
   int L[m+1][n+1];

   for (int i=0; i<=m; i++)
   {
     for (int j=0; j<=n; j++)
     {
       if (i == 0 || j == 0)
         L[i][j] = 0;
       else if (X[i-1] == Y[j-1])
         L[i][j] = L[i-1][j-1] + 1;
       else
         L[i][j] = max(L[i-1][j], L[i][j-1]);
     }
   }

   int idx = L[m][n];
   char lcs[idx+1];
   lcs[idx] = '\0';

   int i = m, j = n;
   while (i > 0 && j > 0)
   {
      if (X[i-1] == Y[j-1])
      {
          lcs[idx-1] = X[i-1];
          i--; j--; idx--;    
      }
 
      else if (L[i-1][j] > L[i][j-1])
         i--;
      else
         j--;
   }
 	
   cout<<"Length of LCS is "<<sizeof(lcs)/sizeof(lcs[0])<<endl;
   cout << "LCS of " << X << " and " << Y << " is " << lcs<<endl;

}

int main()
{
	char X[] = "SDJBVBJSDNVKNKFVNKDFBNKDFNKVNKCNSDKVNJSDVBKJDFVB";
	char Y[] = "ASJDBKAFKNRJGHNKNGKDFNVKDNFVKDNFVKNDFJVNDFKJVDFJVNDFVNADKFVKADNFV";
	int m = strlen(X);
	int n = strlen(Y);
	lcs(X, Y, m, n);
	return 0;
}