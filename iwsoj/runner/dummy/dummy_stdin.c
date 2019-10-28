#include <stdio.h>

int numBits(int n) {
    int b,c;
    for (b=1, c = 0; b < n; b<<=1, c++);
    return c;
}

int main(void)
{
    int x;
    scanf("%d", &x);
    printf("It takes %d bits to represent %d\n", numBits(x), x);
}