#include <stdio.h>

int main(){
    
    
    char str[101];
    while(fgets(str,sizeof(str),stdin)){
        printf("%s",str);
    }
}
