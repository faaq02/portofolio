#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void save(int n, FILE *data){
    float score;
    char fName[100], studName[100];
    printf("\nEnter name of file(with extension):\n");
    scanf(" %[^\n]s", fName);
    data = fopen(fName, "w");
    printf("\nHow many students do you have?:\n");
    scanf("%d", &n);
    fprintf(data, "Names & Scores :\n");
    for(int i = 1; i <= n; ++i){
        printf("\nName of student (%d/%d) :\n", i, n);
        scanf(" %[^\n]s", studName);
        printf("Score(%d/%d) :\n", i, n);
        scanf("%f", &score);
        while(score < 0 || score > 100){
            printf("Score is not valid, please re-enter:\n");
            scanf("%f", &score);
        }
        fprintf(data, "%d. %s : %.2f\n", i, studName, score);
    }
    fclose(data);
}

void load(int n, FILE *data){
    float score;
    char ch, fName[100], studName[100];
    printf("\nEnter file name(with extension):\n");
    scanf(" %[^\n]s", fName);
    printf("\n");
    data = fopen(fName, "r");
        if(data == NULL){
            printf("\nFile doesn't exist\n");
        }
    while((ch = fgetc(data))!=EOF){
            printf("%c", ch);
    }
    fclose(data);
}

int main(){
    int size, input, ctn, menu;
    char ch;
    FILE *file;
    printf("Welcome");
    menu :
        printf("\nMenu: \n");
        printf("1. Save file\n");
        printf("2. Load file\n");
        printf("Other numbers to quit\n");
        printf("Input: ");
        scanf("%d", &input);
        switch(input){
            case 1:
            save(size, file);
            goto menu;
            break;
            case 2:
            load(size, file);
            goto menu;
            break;
            default:
            printf("\nSee ya\n");
            break;
        }
    return 0;
}
