#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int gcd(int a, int b) {
	while(a!=b) {
		if (a==b) {
			return (a+100);
		} else if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
	}
}

int main(void)
{
	int a;
	int b;
	while (scanf("%d %d\n",&a,&b)!=EOF) {
		printf("%d\n", gcd(a,b)); 
	}

}