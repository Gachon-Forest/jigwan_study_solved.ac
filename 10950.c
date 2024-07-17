// 백준 10950번
#include <stdio.h>
#pragma warning (disable: 4996)

int main(void)
{
	int i, t, a, b;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
	return 0;
}
