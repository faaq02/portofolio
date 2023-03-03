#include <stdio.h>

int min_value(int num1, int small){
    int minval, bottom = 0;
    if(num1 <= bottom){
        minval = bottom;
    }
    else{
        minval = num1;
    }
    return minval;
}

int max_value(int num1, int big){
    int maxval, upper = 1;
    if(num1 > upper){
        maxval = upper;
    }
    else{
        maxval = num1;
    }
    return maxval;
}

int main (){
    int counter, size, total, min, max, num, num1;
    printf("how many numbers ya got?\n");
    scanf("%d", &size);
    printf("enter numbers 1/%d :\n", size);
    scanf("%d", &num1);
    min = num1;
    max = num1;
    total = num1;
    for(counter = 2; counter <= size; counter++) {
        printf("enter numbers %d/%d :\n", counter, size);
        scanf("%d", &num);
        total + num;
    }
    int less = min_value(num, min);
    int more = max_value(num, max);
    printf("the min is %d\n", less);
    printf("the max is %d\n", more);

return 0;
}
