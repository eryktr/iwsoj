#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void calculate(float a, float b, float c) {
	float delta = b * b - 4 * a * c;
	float result = 0.0f;
	if (a==0.0f && b==0.0f) {
		printf("a or b must be different by 0\n");
	} else if (a==0.0f && b!=0.0f) {
		result = -c/b;
		printf("%f\n",result);
	} else if (a!=0.0f && delta<0.0f) {
		printf("Delta must be at least 0\n");
	} else if (a!=0.0f && delta==0.0f) {
		result = -b/a;
		printf("%f\n",result);
	} else {
		delta = sqrt(delta);
		result = (-b + delta)/(2*a);
		printf("%f\n",result);
		result = (-b - delta)/(2*a);
		printf("%f\n",result);
	}
}

int main(void)
{
	float a;
	float b;
	float c;
	while (scanf("%f %f %f\n", &a, &b, &c)!=EOF) {
		calculate(a,b,c); 
	}

}