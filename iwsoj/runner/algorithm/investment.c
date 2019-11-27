#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int tax(float interests) {
	int base = (int) (interests + 0.5f);
	int tax = (int) ((0.19f * (float)base) + 0.5f);
	return tax;
}

int main(void) {
	float capital;
	float percent;
	float interests;
	while (scanf("%f %f\n", &capital, &percent)!=EOF){
		interests = capital * (percent / 100.0f);
		interests = interests - tax(interests);
		printf("%.2f\n", interests);
	}
}