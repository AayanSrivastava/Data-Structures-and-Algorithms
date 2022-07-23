/*takes something returns something
//passing and returning structure variable
#include<stdio.h>
struct sum		//creating datatype sum
{
	int km;
	int m;
};
struct sum add(struct sum,struct sum);			//function declaration
int main()
{
	struct sum a1,a2,c;
	scanf("%d%d%d%d",&a1.km,&a2.km,&a1.m,&a2.m);
	c=add(a1,a2);
	printf("%d %d",c.km,c.m);
}
struct sum add(struct sum l1,struct sum l2)		//function definition
{
	struct sum sum1;
	sum1.km=l1.km+l2.km;
	sum1.m=l1.m+l2.m;
	return sum1;	
}
//passing structure variable into function
#include<stdio.h>
#include<stdlib.h>
struct student{
	char name[10];
	int roll;
	long long id;
};
void display(struct student);
int main()
{
	struct student s;
	printf("Enter name,roll no,id of student\n");
	gets(s.name);
	fflush(stdin);
	scanf("%d",&s.roll);
	fflush(stdin);
	scanf("%lld",&s.id);
	display(s);
}
void display(struct student p)
{
	printf("%s %d %lld",p.name,p.roll,p.id);
}
//passing array of structure into function
#include<stdio.h>
#include<stdlib.h>
struct student{
	char name[10];
	int roll;
	long long id;
};
void display(struct student []);
int main()
{
	struct student s[3];
	int i;
	for(i=0;i<3;i++)
	{
		printf("Enter name,roll no,id of student\n");
		fflush(stdin);
		gets(s[i].name);
		fflush(stdin);
		scanf("%d",&s[i].roll);
		fflush(stdin);
		scanf("%lld",&s[i].id);
	}
	display(s);
	return 0;
}

void display(struct student p[])
{
	int i;
	for(i=0;i<3;i++)
	{
		printf("%s %d %lld\n",p[i].name,p[i].roll,p[i].id);
	}
}*/
