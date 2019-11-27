#include<stdio.h>
#include<stdlib.h>

int binarySearch(int table[], int left, int right, int x, int *counter) {
	if (right >= left) {
		int middle = left + (right - left) / 2;
		(*counter)++;
		if (table[middle] == x) {
			printf("%d %d\n", middle, *counter);
			return middle;
		} else if (table[middle] > x) {
			return binarySearch(table, left, middle - 1, x, counter);
		} else {
			return binarySearch(table, middle + 1, right, x, counter);
		}
	}
	printf("The element not exists in table!\n");
}

int main(void) {
	int n;
	int min;
	int max;
	int x;
	int a;
	int j;
	int counter;
	while(scanf("%d %d %d\n",&min,&max,&x)!=EOF) {
		n = max - min + 1;
		j = 0;
		counter = 0;
		if (n<1) {
			printf("Uncorrect number of parameters!\n");
		} else if (min > max) {
			printf("Error: min is greater than max!\n");
		} else {
			int table[n];
			for (int i=min; i<=max; i++) {
				table[j]=i;
				j++;
			}
			a = binarySearch(table, 0, n-1, x, &counter);
		}

	}
	
}