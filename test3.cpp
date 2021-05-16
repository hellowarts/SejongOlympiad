#include <stdio.h>
int main(void) {
	int n,g,time,count;
	int m[100000];
	int i;
	scanf(" %d",&n);
	for(i=0; i<n; i++) {
		scanf(" %d", &m[i]);
	}
	scanf(" %d",&g);
	count = 0;
	time = 0;
	while(count < g) {
		time++;
		for(i=0; i<n; i++) {
			if(time % m[i] == 0){
				count++;
			}
		}
	}
	printf("%d",time);
}
