#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int fibonacci(unsigned int n) {
	if (n<2) {
		return n;
	} else {
		return fibonacci(n-1)+fibonacci(n-2);
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
			fprintf(wFile,"%d\n",fibonacci(number));
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}
