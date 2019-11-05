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

int main(void)
{
	
	int n;
	while (scanf("%d\n",&n)!=EOF) {
		printf("%d\n",fibonacci(n)); 
	}

}
