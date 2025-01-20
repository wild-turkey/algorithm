#include <stdio.h>
#include <stdlib.h>

int main(){
    
    int t,a,b;
    
    scanf("%d",&t);
    
    int * arr = (int*)malloc(t*sizeof(int));
    
    for(int i=0;i<t;i++){
        
        scanf("%d %d",&a,&b);
        arr[i]=a+b;
        
    }
    
    for(int i=0;i<t;i++){
        
        printf("%d\n",arr[i]);
    }
}
