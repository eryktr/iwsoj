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

int coprime(int n) {
    if (n<1){
        fprintf(stderr, "Parameter must be over 0");
    }
    int counter = 0;
    for (int i=1; i<n; i++) {
        if (gcd(i,n)==1) {
            counter++;
        }
    }
    return counter;
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