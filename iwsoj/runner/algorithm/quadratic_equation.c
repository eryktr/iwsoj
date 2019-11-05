#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void calculate(FILE *wFile, float a, float b, float c) {
	float delta = b * b - 4 * a * c;
	float result = 0.0f;
	if (a==0.0f && b==0.0f) {
		fprintf(wFile, "a or b must be different by 0\n");
	} else if (a==0.0f && b!=0.0f) {
		result = -c/b;
		fprintf(wFile,"%f\n",result);
	} else if (a!=0.0f && delta<0.0f) {
		fprintf(wFile,"Delta must be at least 0\n");
	} else if (a!=0.0f && delta==0.0f) {
		result = -b/a;
		fprintf(wFile,"%f\n",result);
	} else {
		delta = sqrt(delta);
		result = (-b + delta)/(2*a);
		fprintf(wFile,"%f\n",result);
		result = (-b - delta)/(2*a);
		fprintf(wFile,"%f\n",result);
	}
}

int main(int argc, char *argv[]){
	char *rFile_name;
	char *wFile_name;
	FILE *rFile;
	FILE *wFile;
	int a;
	int b;
	int c;
	if (argc>=3) {
		rFile_name = argv[1];
		wFile_name = argv[2];
		rFile = fopen(rFile_name,"r");
		wFile = fopen(wFile_name,"w");
		if (rFile==NULL) {
            fprintf( stderr, "error\n");
            return 1;
        }
		if (wFile==NULL) {
            fprintf( stderr, "error\n");
            return 1;			
		}
		while (fscanf(rFile, "%d", &a) > 0)
        {
			if (fscanf(rFile, "%d", &b) > 0) {
				if (fscanf(rFile, "%d", &c) > 0) {
					calculate(wFile,a,b,c);
				}
			}
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}