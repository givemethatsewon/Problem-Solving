#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void swap(int*, int*);

int main(void) {
	// �� ���� �Է¹ޱ�
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	// ������������ a, b, c�� ����ֱ� - ����Ž��
	if (a > b) {
		swap(&a, &b); // a < b ����
	}
	if (b > c) {
		swap(&b, &c); // a < b ����
	}
	if (a > b) {
		swap(&a, &b); // a < b ����
	}
	printf("%d %d %d", a, b, c);
}

void swap(int* pa, int* pb) {
	
	int temp;
	temp = *pa;
	*pa = *pb;
	*pb = temp;
}