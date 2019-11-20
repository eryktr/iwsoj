#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void cash_mashine(float value) {
	float euro[9] = { 600.0f, 300.0f, 150.0f, 60.0f, 15.0f, 8.0f,
	6.0f, 4.0f, 3.0f};
	float cents[6] = { 0.9f, 0.7f, 0.4f, 0.09f, 0.07f, 0.001f };
	int i = 0;
	while (value>=1.0) {
		while (value>=euro[i]) {
			value = value - euro[i];
			printf("%0.0f\n", euro[i]);
		}
		i++;
	}
	i = 0;
	while (value>=0.00099) {
		while (value>=cents[i]-0.00001) {
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