#include<stdio.h>

int main() {
    int arr1[20]={10,20,30,40,50,60};
    int size = 6; // current size of the array
    int newElement = 70; // element to be inserted at the end

    // insert the new element at the end of the array
    arr1[size] = newElement;
    size++; // increment the size of the array

    // print the updated array
    for(int i=0; i<size; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    return 0;
}