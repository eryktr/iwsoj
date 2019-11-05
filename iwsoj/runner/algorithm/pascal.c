#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int coefficient(int n, int k) {	
	if (k > n - k) {
		k = n - k;
	}
	int result = 1;
	for (int i=0; i<k; ++i) {
		result = result * (n - i);
		result = result / (i + 1);
	}
	return result;
}

void printTriangle(FILE *wFile, int n) {
    for (int i = 0; i < n; i++) 
    {
		for (int j = 0; j <= i; j++) { 
            fprintf(wFile,"%d ", coefficient(i, j));
		}
        fprintf(wFile,"\n"); 
    } 
}

int main(int argc, char *argv[]){
	char *rFile_name;
	char *wFile_name;
	FILE *rFile;
	FILE *wFile;
	float number;
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
		while (fscanf(rFile, "%f", &number) > 0)
        {
			if (number>=1 && number<=30) {
				printTriangle(wFile, number);
			} else if (number>30) {
				fprintf(wFile,"Parameter is too much!\n");
			} else {
				fprintf(wFile,"Parameter is below 1!\n");
			}
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}