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
				fprintf(wFile,"%d\n",gcd(a,b));
			}
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}