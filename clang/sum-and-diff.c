#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int one_i = 0;
	int two_i = 0;
	float one_f = 0.0;
	float two_f = 0.0;

	scanf("%d %d", &one_i, &two_i);
	scanf("%f %f", &one_f, &two_f);

    printf("%d %d\n", (one_i + two_i), (one_i - two_i));
	printf("%.1f %.1f\n", (one_f + two_f), (one_f - two_f));
    return 0;
}