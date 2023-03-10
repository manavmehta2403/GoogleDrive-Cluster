#include <stdio.h>

int main()
{
    //printf("Hello World");

    int a;
    int *p;
    
    a = 6;
    p = &a;
    
    printf("%d",&p);
    printf("\n");
    printf("%d",&a);
    printf("\n");
    printf("%d",p);
    printf("\n");
    printf("%d",*p);
    printf("\n");
    printf("%d",a);
    
    return 0;
}
