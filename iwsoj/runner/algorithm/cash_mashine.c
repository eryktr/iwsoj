#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void cash_mashine(float value) {
	float euro[9] = { 500.0f, 200.0f, 100.0f, 50.0f, 20.0f, 10.0f,
	5.0f, 2.0f, 1.0f};
	float cents[6] = { 0.5f, 0.2f, 0.1f, 0.05f, 0.02f, 0.01f };
	int i = 0;
	while (value>=1.0) {
		while (value>=euro[i]) {
			value = value - euro[i];
			printf("%0.0f\n", euro[i]);
		}
		i++;
	}
	i = 0;
	while (value>=0.0099) {
		while (value>=cents[i]-0.0001) {
			value = value - cents[i];
			printf("%0.2f\n", cents[i]);
		}
		i++;
	}	
	
}

int main(void)
{
	float n;
	while (scanf("%f\n",&n)!=EOF) {
		cash_mashine(n); 
	}

}