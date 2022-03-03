#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    char d,q='\0';
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    for(int i=0;d[i]!='\0';i++)
    {
        if(d[i]!=' ')
        {
            q=q+d[i];
        }
        else{
            printf("%s\n",q);
        }
        }
    return 0;
}
