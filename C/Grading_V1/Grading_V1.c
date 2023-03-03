#include <stdio.h>

char grade(float n){
    char sym;
    if(n >= 85 && n <= 100){
        sym = 'A';
    }
    else if(n >= 70 && n < 85){
        sym = 'B';
    }
    else if(n >= 60 && n < 80){
        sym = 'C';
    }
    else if(n >= 55 && n < 60){
        sym = 'D';
    }
    else{
        sym = 'E';
    }
return sym;
}

int main (){
    int result, size, counter = 1;
    float num;
    printf("how many scores do you have?\n");
    scanf("%d", &size);
    while(counter <= size){
        printf("enter the score (%d):\n", counter);
        scanf("%f", &num);
        while(num < 0 || num > 100){
            printf("that aint right, 0 to 100 only. try again : \n");
            scanf("%f", &num);
        }
        char result = grade(num);
        printf("the grade is :\n");
        printf("%c\n", result);
        counter++;
    }
return 0;
}

