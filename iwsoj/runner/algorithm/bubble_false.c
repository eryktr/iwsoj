#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void swap(int *x, int *y, int *counter) {
	int tmp = *x;
	*x = *y;
	*y = tmp;
	(*counter)++;
}

void bubble(int arr[], int n, int *counter) {
	for (int i=0; i<(n-1); i++) {
		for (int j=0; j<(n-i-1); j++) {
			if (arr[j] > arr[j+1]) {
				swap(&arr[j],&arr[j+1],counter);
			}
		}
	}
	
}

int main(void) {
	int n;
	int a;
	int counter = 100;
	scanf("%d\n",&n);
	if (n<1) {
		fprintf(stderr,"Uncorrect number of parameters");
	}
	int table[n];
	for (int i=0; i<n; i++) {
		scanf("%d\n",&a);
		table[i]=a;
	}
	bubble(table, n, &counter);
	printf("%d\n",counter);
	
}