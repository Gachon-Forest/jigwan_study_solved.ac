// 백준 2438번
#include <stdio.h>
#pragma warning (disable: 4996)

int main(void)
{
	int i, j, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
