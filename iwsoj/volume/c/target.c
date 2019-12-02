#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int prime(int n) {
  if (n<2) {
    return 0;
  } else {
    int counter = 0;
    for (int i=2; i<=n; i++) {
      counter++;
      for (int j=2; j*j<=i; j++) {
        if (i%j==0) {
          counter--;
          break;
		}
      }
    }
    return counter;
  }       
	
}

int main(void)
{
	int n;
        while (scanf("%d\n",&n)!=EOF) {
		printf("%d\n", prime(n)); 
	}

}