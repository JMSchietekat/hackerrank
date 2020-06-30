#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char* intToString(int input){
	switch(input){
		case 1: return "one";
		case 2: return "two";
		case 3: return "three";
		case 4: return "four";
		case 5: return "five";
		case 6: return "six";
		case 7: return "seven";
		case 8: return "eight";
		case 9: return "nine";
		default: return "Greater than 9";
	}
}

int main()
{	
	int input = 0;
	scanf("%i", &input);

    printf("%s\n", intToString(input));
    return 0;
}