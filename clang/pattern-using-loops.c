#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void printGrid(int *arr, int size){
	int i, j; 
		for (i = 0; i < size; i++) 
			for (j = 0; j < size; j++) 
				printf("%d ", arr[i][j]);
}

int main() 
{

    int n;
    scanf("%d", &n);

	const int size = 2*n-1;

	int grid[size][size] = {0};
  	
	printGrid(grid, size);

    return 0;
}