#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,n1,i=0;
	char *p,*p1;
	scanf("%d",&n);
	p=(char*)malloc(n*sizeof(char));
	scanf("%d",&n1);
	p1=(char*)malloc(n1*sizeof(char));
	printf("Enter the string=");
	fflush(stdin);
	gets(p);
	while(*(p+i)!='\0')
	{
		*(p1+i)=*(p+i);
		i++;
 	}
 	*(p1+i)='\0';
 	printf("%s",p1);
 	free(p);
 	free(p1);
	return 0;
}
