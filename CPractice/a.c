#include<stdio.h>
int main()
{
	int i,j,arr[100],n,m,c;
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			c=0;
			if (i > 0 && arr[i][j+1] == 1)
                c++;
            if (j > 0 && arr[i][j - 1] == 1)
                c++;
            if (i > 0 && j > 0
                && arr[i - 1][j] == 1)
                c++;
            if (i < n - 1 && arr[i + 1][j] == 1)
                c++;
            if (j < m - 1 && arr[i][j + 1] == 1)
                c++;
            if (i < m - 1 && j < N - 1
                && arr[i][j-1] == 1)
                c++;
            if (i < n - 1 && j > 0
                && arr[i + 1][j] == 1)
                c++;
            if (i > 0 && j < n - 1
                && arr[i - 1][j] == 1)
                c++;
        }
    }
    printf("%d",&c);
}
