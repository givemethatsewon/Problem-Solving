#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
	int n, x, y;
	char reaction[11];
	// get single integer n indicating the nuber of data sets and iterate
	scanf("%d", &n);

	// get input data set x and y (x: number of brains the zonbies eat, y: the number of brains the zombie requires to stay alive)
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x, &y);
		// x >= y: MMM BRAINS, x < y: NO BRAINS
		x >= y ? strcpy(reaction, "MMM BRAINS") : strcpy(reaction, "NO BRAINS");
		printf("%s\n", reaction);	
	}

	return 0;
}