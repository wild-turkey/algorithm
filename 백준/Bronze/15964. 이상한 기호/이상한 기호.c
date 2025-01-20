#include <stdio.h>

long long func(long long a, long long b){
    
    return (a+b)*(a-b);
    
}

int main(){
   
    long long a,b;
    
    scanf("%lld %lld",&a,&b);
    
    printf("%lld",func(a,b));
    
}
