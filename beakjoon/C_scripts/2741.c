#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	//n �Է¹ޱ�
	int n;
	scanf("%d", &n);

	//�ݺ������� 1�� ������Ű�鼭 ���
	for (int i = 1; i <= n; i++) {
		printf("%d\n", i);
	}

	return 0;
}