#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void cash_mashine(FILE *wFile, float value) {
	float euro[9] = { 500.0f, 200.0f, 100.0f, 50.0f, 20.0f, 10.0f,
	5.0f, 2.0f, 1.0f};
	float cents[6] = { 0.5f, 0.2f, 0.1f, 0.05f, 0.02f, 0.01f };
	int i = 0;
	while (value>=1.0) {
		while (value>=euro[i]) {
			value = value - euro[i];
			fprintf(wFile,"%0.0f\n", euro[i]);
		}
		i++;
	}
	i = 0;
	while (value>=0.0099) {
		while (value>=cents[i]-0.0001) {
			value = value - cents[i];
			fprintf(wFile,"%0.2f\n", cents[i]);
		}
		i++;
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
			cash_mashine(wFile, number);
        }
		fclose(rFile);
		fclose(wFile);

	}
	
}