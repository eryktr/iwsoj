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

int coprime(int n) {
    if (n<1){
        fprintf(stderr, "Parameter must be over 0");
    }
    int counter = 0;
    for (int i=1; i<n; i++) {
        if (gcd(i,n)==1) {
            counter++;
        }
    }
    return (counter+100);
}

int main(void)
{
	int n;
	while (scanf("%d\n",&n)!=EOF) {
		printf("%d\n", coprime(n)); 
	}

}