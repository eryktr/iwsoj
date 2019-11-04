#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int gcd(int a, int b) {
	while(a!=b) {
		if (a==b) {
			return a;
		} else if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
	}
}

int main(void){
	int a = 256;
	int b = 576;
	printf("There Greatest Common Divisor of %d and %d is %d\n", a, b, gcd(a,b));
}