#include<stdio.h>

int main(void) {
	int hour, minute;
	int m[5];
	int i;
	scanf(" %d %d", &hour, &minute);
	for(i = 0; i<5; i++) {
		scanf(" %d",&m[i]);
	}
	
	for(i=0; i<5; i++) {
		minute += m[i];
		hour += minute / 60;
		minute %= 60;
		hour %= 24;
	}
	printf("%d %d",hour, minute);
}
