main()
{
	int a,b,s;
	scanf("%d%d",&a,&b);
	s=gcd(a,b);
	printf("%d",s);
}
int gcd(int a,int b)
{
	int q,w,c;
	q=a>=b?a:b;
	w=a<=b?a:b;
	c=q%w;
	if(c==0)
	return w;
	else
	return gcd(w,c);
}
