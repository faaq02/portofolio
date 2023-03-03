#include <stdio.h>

int main (){
    int total, min, max, size, counter, num, num1;
    printf("welcome to auto min max\n");
    printf("how many numbers do you have?\n");
    scanf("%d", &size);
    printf("lets go 1/%d :\n", size);
    scanf("%d", &num1);
    min = num1;
    max = num1;
    total = num1;
    for(counter = 2; counter <= size; counter++){
        printf("lets go %d/%d :\n", counter, size);
        scanf("%d", &num);
        total + num;
        if(num > max) max = num;
        if(num < min) min = num;
    }
    printf("\n");
    printf("min is %d\n", min);
    printf("max is %d\n", max);

return 0;
}
