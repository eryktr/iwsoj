#include<stdio.h>
#include<stdlib.h>

void triangle(int n) {
	for (int i=1; i<=n; i++) {
		int counter = 1;
		for (int j=n; j>=i; j--) {
			printf("a");
		}
		while (counter<=i) {
			printf("*b");
			counter++;
		}
		printf("\n");
	}
}

int main(void)
{
	int n;
	while (scanf("%d\n",&n)!=EOF) {
		triangle(n); 
	}

}