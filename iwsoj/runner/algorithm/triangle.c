#include<stdio.h>
#include<stdlib.h>

void triangle(FILE *wFile, int n) {
	for (int i=1; i<=n; i++) {
		int counter = 1;
		for (int j=n; j>=i; j--) {
			fprintf(wFile," ");
		}
		while (counter<=i) {
			fprintf(wFile,"* ");
			counter++;
		}
		fprintf(wFile,"\n");
	}
}

int main(int argc, char *argv[]){
	char *rFile_name;
	char *wFile_name;
	FILE *rFile;
	FILE *wFile;
	int number;
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
		while (fscanf(rFile, "%d", &number) > 0)
        {
			triangle(wFile, number);
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}