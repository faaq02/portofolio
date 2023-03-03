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
    int result, size, counter = 1, aCount = 0, bCount = 0, cCount = 0, dCount = 0, eCount = 0;
    float num, average, total = 0;
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
        switch(result){
            case 'A': ++aCount;
            break;
            case 'B': ++bCount;
            break;
            case 'C': ++cCount;
            break;
            case 'D': ++dCount;
            break;
            case 'E': ++eCount;
            break;
        }
        printf("the grade is :\n");
        printf("%c\n", result);
        average = (total += num) / size;
        counter++;
    }
    printf("\n");
    printf("score average is %.2f\n", average);
    printf("\n");
    printf("grade totals:\n");
    printf("A: %d\n", aCount);
    printf("B: %d\n", bCount);
    printf("C: %d\n", cCount);
    printf("D: %d\n", dCount);
    printf("E: %d\n", eCount);

return 0;
}

