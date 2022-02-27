#include<stdio.h>
#include<string.h>
int main()
{
    int i,j,k,l;
    char s[100];
    scanf("%s",s);
    for(i=0;s[i]!='\0';i++)
    {
        for(j=i+1;s[j]!='\0';j++)
        {
            if(s[i]==s[j])
            {
                for(k=i;s[k];k++)
                {
                    s[k]=s[k+1];
                }
                j--;
            }
        }
    }
    l=strlen(s);
    if(l==0)
    printf("Empty string");
    else
    printf("%s",s);
}
