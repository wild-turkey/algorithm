#include <stdio.h>

int main(){
    
    int arr[28],i,k,val;
    
    for(i=0;i<28;i++){
        scanf("%d",&arr[i]);
    }
    
    for(i=1;i<31;i++){
        for(k=0;k<28;k++){
            if(arr[k]==i){
                val=1;
                break;
            }
                else val = 0;
        }
        
        if(val == 0) printf("%d\n",i);
    }
    
}
