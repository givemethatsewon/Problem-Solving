#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void swap(int*, int*);

int main(void) {
	// 수 세개 입력받기
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	// 오름차순으로 a, b, c에 집어넣기 - 선형탐색
	if (a > b) {
		swap(&a, &b); // a < b 보장
	}
	if (b > c) {
		swap(&b, &c); // a < b 보장
	}
	if (a > b) {
		swap(&a, &b); // a < b 보장
	}
	printf("%d %d %d", a, b, c);
}

void swap(int* pa, int* pb) {
	
	int temp;
	temp = *pa;
	*pa = *pb;
	*pb = temp;
}