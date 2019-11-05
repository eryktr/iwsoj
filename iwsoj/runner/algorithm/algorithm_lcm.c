#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int lcm(int a, int b) {
	if (a==0 || b==0) {
		fprintf(stderr, "Math error: Paramaters must't be equal 0!");
	}
	
	int ab = a * b;
	int c = a;
	while(a!=b) {
		if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
		c = a;
	}
	return ab/c;
}

int main(int argc, char *argv[]){
	char *rFile_name;
	char *wFile_name;
	FILE *rFile;
	FILE *wFile;
	int a;
	int b;
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
				fprintf(wFile,"%d\n",lcm(a,b));
			}
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}