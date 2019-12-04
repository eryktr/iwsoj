#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int isPrime(int value) {
	int border = (int) sqrt(value);
	for (int i=2; i<=border; i++) {
		if (value % border == 0) {
			return 0;
		}	
	}
	return 1;

}

void factors(int n) {
	int value = 2;
	if (n < 2) {
		printf("Number is below 2");
	} else {
		while (n>=2) {
			while (n % value == 0) {
				n = n / value;
				printf("%d\n",value);
			}
			value++;
			while (isPrime(value)==0) {
				value++;
			}
		}
	}
}

int main(void) {
	int n;
	while (scanf("%d\n",&n)!=EOF) {
		factors(n); 
	}
}