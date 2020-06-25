#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_ARR_LENGHT 10000

int *initArr(int n)
{
	static int arr[MAX_ARR_LENGHT];

	for (int i = 0; i < n; i++)
	{
		arr[i] = i + 1;
	}

	return arr;
}

int bw_andFn(int a, int b)
{
	return a & b;
}

int bw_orFn(int a, int b)
{
	return a | b;
}

int bw_xorFn(int a, int b)
{
	return a ^ b;
}

int process(int n, int k, int *s, int (*fn)(int a, int b))
{
	int max_lt_k = 0;

	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			int temp = fn(s[i], s[j]);
			// printf("a[%i]=%i b[%i]=%i a?b=%i\n", i, s[i], j, s[j], temp);
			if (temp > max_lt_k && temp < k)
			{
				max_lt_k = temp;
			}
		}
	}

	return max_lt_k;
}

int main(void)
{
	int n = 0;
	int k = 0;
	int *s;
	scanf("%i %i", &n, &k);

	s = initArr(n);

	int bw_and = process(n, k, s, *bw_andFn);
	int bw_or = process(n, k, s, *bw_orFn);
	int bw_xor = process(n, k, s, *bw_xorFn);

	printf("%i\n%i\n%i\n", bw_and, bw_or, bw_xor);
}