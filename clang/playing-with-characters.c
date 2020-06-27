#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LEN 100

int main() 
{

    char ch;
    scanf("%c", &ch);
    
    char s[MAX_LEN];
    scanf("%s", &s);

    char sen[MAX_LEN];
    scanf(" %[^\n]%*c", sen);    
    
    printf("%c\n", ch);  
    printf("%s\n", s);  
    printf("%s\n", sen);  
    return 0;
}

