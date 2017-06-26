#include<stdio.h>
#include<stdlib.h>

void towers(int, char, char, char);

void main()
{
	system("cls");
	int n;
	printf("Enter the number of disks: ");
	scanf("%d", &n);

	towers(n, 'A', 'C', 'B');
}

void towers(int n, char from, char to, char aux)
{
	if(n==1)
	{
		printf("\n%s%c%s%c", "move disk 1 from peg ", from, " to peg ", to);
		return;
	}

	towers(n-1, from, aux, to);
	printf("\n%s%d%s%c%s%c", "move disk ", n, " from peg ", from, " to peg ", to);
	towers(n-1, aux, to, from);
}