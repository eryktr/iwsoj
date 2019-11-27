#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int average(int n, float table[n]) {
	float total = 0.0f;
	for (int i=0; i<n; i++) {
		total = total + table[i];
	}
	return (int) (total/n + 0.5f);
}

int main(void) {
	int n;
	float a;
	scanf("%d\n",&n);
	if (n<1) {
		fprintf(stderr,"Uncorrect number of parameters");
	}
	float table[n];
	for (int i=0; i<n; i++) {
		scanf("%f\n",&a);
		table[i]=a;
	}
	n = average(n, table);
	printf("%d\n", n);
	
}