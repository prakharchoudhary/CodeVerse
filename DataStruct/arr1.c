#include<stdio.h>

int main(){
    int arr[20],size,i;
    char ch;
    printf("Enter the size of array: ");
    scanf("%d",&size);
    printf("Enter the elements in array:\n");
    for(i=0; i<size; i++){
        scanf("%d", &arr[i]);
    }
    printf("The array is: \n");
    for(i=0; i<size; i++){
            printf("%d ", arr[i]);
    }
 
}
