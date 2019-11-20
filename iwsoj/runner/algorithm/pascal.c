#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int coefficient(int n, int k) {	
	if (k > n - k) {
		k = n - k;
	}
	int result = 1;
	for (int i=0; i<k; ++i) {
		result = result * (n - i);
		result = result / (i + 1);
	}
	return result;
}

void printTriangle(int n) {
    for (int i = 0; i < n; i++) 
    {
		for (int j = 0; j <= i; j++) { 
            printf("%d ", coefficient(i, j));
		}
        printf("\n"); 
    } 
}

int main(void)
{
	int n;
	while (scanf("%d\n",&n)!=EOF) {
		if (n>=1 && n<=30) {
			printTriangle(n);
		} else if (n>30) {
			printf("Parameter is too much!\n");
		} else {
			printf("Parameter is below 1!\n");
		} 
	}

}