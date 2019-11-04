#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int fibonacci(unsigned int n) {
	if (n<2) {
		return n;
	} else {
		return fibonacci(n-1)+fibonacci(n-2);
	}
}

int main(void){
	unsigned int n = 23;
	printf("The %d number of Fibonacci is %d\n", n, fibonacci(n));
}