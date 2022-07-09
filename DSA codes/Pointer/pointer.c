#include<stdio.h>
// int main()
// {
    // POINTERS ARITHMATIC

    // int n=5;
    // int *p=&n;
    // printf("%d ",p);
    // *p++;
    // printf("%d",p);
    // int *q=p;
    // printf("%d %d",*q,*p);
    // printf("%d\n",(*p)++); //changes_value for later use
    // printf("%d\n",++*p); //changes_value for current use
    // printf("%d\n",*p++); //changes_address_location_to_next
    // printf("%d\n",p);
    // *p=*p+1;
    // printf("%d",p);

    // ARRAY POINTERS

    // int ar[10]={1,2,3};
    // int *p=ar;
    // *p=*p+1;
    // printf("%d\n",*(ar+1));
    // printf("%d\n",ar+2);
    // printf("%d\n",*p);
    // printf("%d\n",*p++);

    //character pointer

    // char ch[6]="abcde";
    // char *c=&ch[0];
    // printf("%s",ch);
// }

//Function And Pointers
// void update(int *p)  //udates value in this scope only
// {
//     p=p+1;
// }
// void update1(int *p)  //udates value globally
// {
//     *p=*p+1;
// }
// int main()
// {
//     int n=5;
//     int *p=&n;
//     printf("%d\n",*p);
//     update(&n);
//     printf("%d\n",*p);
// }

// int getsum(int *ar,int n)
// {
//     printf("%d\n",sizeof(ar));
//     int sum=0,i;
//     for(i=0;i<n;i++)
//     {
//         sum+=ar[i];
//     }
//     return sum;
// }
// int main()
// {
//     int ar[6]={1,2,3,4,5};
//     printf("%d\n",sizeof(ar));
//     printf("%d",getsum((ar+3),3));
// }


// Double Pointers

// void update(int **p)
// {
//     // p=p+1; // no change

//     // *p=*p+1; //n changes

//     **p=**p+1;
//     // *x+=1;
// }

// int main()
// {
//     int n=5;
//     int* p=&n;
//     int **q = &p;
//     // printf("%d %d %d %d",*p,p,**q,q);
//     printf("%d %d %d\n",n,p,q);
//     update(q);
//     printf("%d %d %d",n,p,q);
// }

// int main()
// {
//     void* p;
//     int i=5;
//     p=&i;
//     printf("%d\n",*(int*)p);
// }

// int main()
// {
//     char b[] = "xyz";
//     char *c = b;
//     printf("%c",c[0]);
// }

// int main()
// {
//   char arr[20];
//   int i;
//   for(i = 0; i < 10; i++) {
//     *(arr + i) = 65;
//   }
//   *(arr + i) = '\0';
//   printf("%s ",arr);
//   return 0;
// }

//Typecasted
// int main() {
//   char st[] = "ABCD";
//   for(int i = 0; st[i] !='\0';i++) {
//      printf("%c %d %c %c", st[i] ,*(st)+i,*(i+st),i[st]);
//   }
//   return 0;
// }

void swap (char *x, char *y) 
{
  char *t = x;
  x = y;
  y = t;
  printf("%s %s\n",x,y);
}

int main()
{
   char *x = "geeksquiz";
   char *y = "geeksforgeeks";
   char *t;
   swap( x, y);
   printf("%s %s\n",x,y);
   t = x;
   x = y;
   y = t; 
   printf(" %s %s",x,y);
   return 0;
}