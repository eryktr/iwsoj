#include <stdio.h>
#include <stdlib.h>

float bmi(float growth, float mass) {
	if (growth<=0.0f || mass<=0.0f) {
		fprintf(stderr,"Growth or mass is incorrect");
	}
	growth = growth/100.0f;
	return (mass/(growth*growth));
}

int main(void) {
	float growth;
	float mass;
	while (scanf("%f %f\n", &growth, &mass)!=EOF) {
		if (bmi(growth, mass)>=30.0f) {
			printf("obesity\n");
		} else if (bmi(growth, mass)>=25.0f) {
			printf("overweight\n");
		} else if (bmi(growth, mass)>=18.5f) {
			printf("healthy mass\n");
		} else {
			printf("underweight\n");
		}
	}
}