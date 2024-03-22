#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	//n 입력받기
	int n;
	scanf("%d", &n);

	//반복문으로 1씩 증가시키면서 출력
	for (int i = 1; i <= n; i++) {
		printf("%d\n", i);
	}

	return 0;
}