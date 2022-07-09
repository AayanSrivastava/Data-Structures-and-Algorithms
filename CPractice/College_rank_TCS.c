#include<stdio.h>

struct stu
{
	int id;
	float per;
	int c1,c2,c3;
};

int main()
{
	struct stu s[1000];
	int n,c,c1[100],i;
	scanf("%d %d",&n,&c);
	for(i=0;i<n;i++)
	{
		scanf("%d",&c1[i]);
	}
	for(i=0;i<c;i++)
	{
		scanf("%d %f %d %d %d",&s[i].id,&s[i].per,&s[i].c1,&s[i].c2,&s[i].c3);
	}
	for(i=0;i<c;i++)
	{
		printf("%Student-d,%f,%d,%d,%d\n",s[i].id,s[i].per,s[i].c1,s[i].c2,s[i].c3);
	}
}
