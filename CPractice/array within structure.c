#include<stdio.h>
struct student
{
	char name[20];
	int roll,marks[3];
};
int main()
{
	struct student s;
	int i,sum=0;
	printf("enter name,roll of students\n");	
	scanf("%s",s.name);
	fflush(stdin);
	scanf("%d",&s.roll);
	printf("enter marks of 2 subjects\n");
	for(i=0;i<2;i++)
	{
	scanf("%d",&s.marks[i]);
	sum+=s.marks[i];
	}
	printf("%s\n",s.name);
	printf("%d\n",s.roll);
	for(i=0;i<2;i++)
	{
	printf("%d\n",s.marks[i]);
	}
	printf("sum=%d\n",sum);
}
