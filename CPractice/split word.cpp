#include<stdio.h>
#include<string.h>  
int main(void) {
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;j++){
	    char s[1001];
	    scanf("%s",s); 
	  //  printf("%s ",s);
	    int l=strlen(s),x=0,k=0;    
	    int c=(l/2)+1;
	    if(l%2==0){
	        c=l/2; 
	        k=c;
	    } 
	    else if(l%2!=0){
	        c=(l/2)+1; 
	        k=c;
	    } 
	    for(int i=0;i<l/2;i++){ 
	        for(k=c;k<l;k++){
	            if(s[i]==s[k]){
	                s[k]='0';
	                x++;   
	                break;
	            }
	        }
	    }  
	    //printf("%d ",x);
	    if(x==l/2){
	        printf("YES\n");
	    } 
	    else {
	        printf("NO\n");
	    }
	} 
	return 0;
}
