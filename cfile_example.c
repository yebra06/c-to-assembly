#include <stdio.h>

struct user {
	int id;
};

int main() {
	int counter = 0;
	while (counter < 10)
		printf("%d\n", counter++);
	return 0;
}

