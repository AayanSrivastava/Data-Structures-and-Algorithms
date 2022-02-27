#include<stdio.h>
int main()
{
	int p,i,t,n[100000],f,q=0,w=0,e=0,r=0,y=0,u=0;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n[i]);
	}
	for(i=0;i<t;i++)
	{
		p=n[i];
		q=p/100;
		p=p-(q*100);
		w=p/50;
		p=p-(w*50);
		e=p/10;
		p=p-(e*10);
		r=p/5;
		p=p-(r*5);
		y=p/2;
		p=p-(y*2);
		u=p/1;
		printf("100=%d\n50=%d\n10=%d\n5=%d\n2=%d\n1=%d\n",q,w,e,r,y,u);
		f=q+w+e+r+y+u;
		printf("\n%d",f);
}
return 0;
}
