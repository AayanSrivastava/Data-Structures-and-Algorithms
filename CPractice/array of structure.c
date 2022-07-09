#include<stdio.h>
struct student
{
	char name[20];
	int roll,marks;
};
int main()
{
	struct student s[5];
	int i;
	for(i=0;i<5;i++)
	{
	printf("enter name,roll and marks of %d students\n",i+1);	
	scanf("%s",s[i].name);
	fflush(stdin);
	scanf("%d",&s[i].roll);
	fflush(stdin);
	scanf("%d",&s[i].marks);
	}
	for(i=0;i<5;i++)
	{
	printf("%s %d %d\n",s[i].name,s[i].roll,s[i].marks);
	}
}
