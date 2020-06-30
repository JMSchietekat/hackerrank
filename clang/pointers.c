#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
	int in_a = *a;
	int in_b = *b;

    *a = in_a + in_b;
	*b = abs(in_a - in_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}