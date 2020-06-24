#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int process(int input){
	int sum = 0;
	do {
		sum += input % 10;
		input /= 10;
		// printf("sum %d, input %d\n", sum, input);
	} while (input >= 10);

	sum += input % 10;

	return sum;
}

int main()
{	
	int n = 0;
	scanf("%d", &n);

	printf("%d", process(n));
    
    return 0;
}