main()
{
	int a,b,s;
	scanf("%d%d",&a,&b);
	s=gcd(a,b);
	printf("%d",s);
}
int gcd(int a,int b)
{
	if(a==b)
	return a;
	if(a%b==0)
	return b;
	if(b%a==0)
	return a;
	if(a>b)
	return (gcd(a%b,b));
	else
	return (gcd(a,b%a));
}
