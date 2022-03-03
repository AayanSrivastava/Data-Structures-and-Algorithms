#include<stdio.h>
struct student
{
	char name[10];
	int roll;
	struct stu_mark
	{
		char sub[10];
		int m;
	}mark;               //have to declare one variable to access the member of inner structure
};
int main()
{
	struct student s;
	printf("Enter name,roll no.,sub,marks\n");
	scanf("%s",s.name);
	scanf("%d",&s.roll);
	scanf("%s",s.mark.sub);
	scanf("%d",&s.mark.m);
	printf("%s %d %s %d",s.name,s.roll,s.mark.sub,s.mark.m);
}
