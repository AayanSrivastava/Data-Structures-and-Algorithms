//takes something returns nothing,something
#include<stdio.h>
typedef struct inp		//creating datatype 
{
	char name[10];
	int roll;
}z;
z input();			//function declaration	 
z input()			
{
	z s1;
	printf("Enter name and roll no.\n");
	scanf("%s",s1.name);
	scanf("%d",&s1.roll);
	return s1;
}
void display(z s)
{
	printf("%d-%s",s.roll,s.name);
}
int main()
{
	z st;
	st=input();
	display(st);
}
