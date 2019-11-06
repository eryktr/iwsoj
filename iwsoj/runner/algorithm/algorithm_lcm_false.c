#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int lcm(int a, int b) {
	if (a==0 || b==0) {
		fprintf(stderr, "Math error: Paramaters must't be equal 0!");
	}
	
	int ab = a * b;
	int c = a;
	while(a!=b) {
		if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
		c = a;
	}
	return (ab/c)+100;
}

int main(void)
{
	int a;
	int b;
	while (scanf("%d %d\n",&a,&b)!=EOF) {
		printf("%d\n", lcm(a,b)); 
	}

}