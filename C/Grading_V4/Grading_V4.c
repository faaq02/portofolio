#include <stdio.h>

typedef struct Student{
    char name[100];
    float score;
    char grade;
}students;

char toLetterGrade(float score){
    char grade;
    if(score >= 85 && score <= 100){
        grade = 'A';
    }
    else if(score >= 70 && score < 85){
        grade = 'B';
    }
    else if(score >= 60 && score < 70){
        grade = 'C';
    }
    else if(score >= 55 && score < 60){
        grade = 'D';
    }
    else{
        grade = 'E';
    }
    return grade;
}

float maximum(float score1, float score2){
    if(score1 > score2){
        score2 = score1;
    }
    return score2;
}

float minimum(float score1, float score2){
    if(score1 > score2){
        score1 = score2;
    }
    return score1;
}

void printData(int num, students student[]){
    for(int i = 0; i < num; i++){
        printf("\n%d. %s %.2f (%c)", i + 1,
               student[i].name, student[i].score,
               student[i].grade);
    }
}

void sortAndPrintAscending(int num, students student[]){
    students temp;
    for(int i = 0; i < num-1; i++){
        for(int j = 0; j < num-i-1; j++){
            if(student[j+1].score < student[j].score){
                temp = student[j+1];
                student[j+1] = student[j];
                student[j] = temp;
            }
        }
    }
    printData(num, student);
}

void sortDescending(int num, students student[]){
    students temp;
    for(int i = 0; i < num-1; i++){
        for(int j = 0; j < num-i-1; j++){
            if(student[j+1].score > student[j].score){
                temp = student[j+1];
                student[j+1] = student[j];
                student[j] = temp;
            }
        }
    }
    printData(num, student);
}

int main(){
    int menu, num;
    float sum = 0, average, maxScore=0, minScore=100;
    students student[999];
    char fileName[100];
    FILE *file;
    printf("Welcome");
    Menu:
    printf("\nWhat do you want to do? :");
    printf("\n1. Enter students data");
    printf("\n2. Count students average score");
    printf("\n3. Count highest & lowest score");
    printf("\n4. Sort scores(Asc)");
    printf("\n5. Sort scores(Dsc)");
    printf("\n6. Write to file");
    printf("\n7. Open from file");
    printf("\n8. Print Data");
    printf("\nOther numbers to quit");
    printf("\n\nInput : ");
    scanf("%d", &menu);

    if(menu == 1){
        printf("\nHow many students? : ");
        scanf("%d", &num);
        for(int i = 0; i < num; i++){
            printf("\nEnter name (%d/%d) : ", i+1, num);
            scanf(" %[^\n]s", student[i].name);
            printf("Enter score : ");
            scanf("%f", &student[i].score);
            while(student[i].score < 0 || student[i].score > 100){
                printf("Invalid value, try again : ");
                scanf("%f", &student[i].score);
            }
            student[i].grade = toLetterGrade(student[i].score);
            sum += student[i].score;
        }
        average = sum / num;
        goto Menu;
    }
    else if(menu == 2){
        printf("\nThe average is : %.2f\n", average);
        goto Menu;
    }
    else if(menu == 3){
        for(int i = 0; i < num; i++){
            maxScore = maximum(student[i].score, maxScore);
            minScore = minimum(student[i].score, minScore);
        }
        for(int i = 0; i < num; i++){
            if(student[i].score == maxScore){
                printf("\nThe highest score is : %s, %.2f (%c)",
                       student[i].name, student[i].score, student[i].grade);
            }
        }
        for(int i = 0; i < num; i++){
            if(student[i].score == minScore){
                printf("\nThe lowest score is : %s, %.2f (%c)\n",
                       student[i].name, student[i].score, student[i].grade);
            }
        }
        goto Menu;
    }
    else if(menu == 4){
        sortAndPrintAscending(num, student);
        printf("\n");
        goto Menu;
    }
    else if(menu == 5){
        sortDescending(num, student);
        printf("\n");
        goto Menu;
    }
    else if(menu == 6){
        printf("\nEnter file name with extension : ");
        scanf(" %[^\n]s", fileName);
        file = fopen(fileName, "a");
        sortDescending(num, student);
        for(int i = 0; i < num; i++){
            fprintf(file, "%.2f %c %s\n", student[i].score, student[i].grade, student[i].name);
        }
        fclose(file);
        goto Menu;
    }
    else if(menu == 7){
        printf("\nEnter file name with extension : ");
        scanf(" %[^\n]s", fileName);
        file = fopen(fileName, "r");
        if(file == NULL){
            printf("\n  FILE NOT FOUND!");
            goto Menu;
        }
        num = 0;
        sum = 0;
        int i = 0;
        fscanf(file, "%f %c %[^\n]s", &student[i].score,
               &student[i].grade, student[i].name);
        while(!feof(file)){
            printf("\n%d. %s %.2f %c", i + 1, student[i].name,
                   student[i].score, student[i].grade);
            sum += student[i].score;
            num++;
            i++;
            fscanf(file, "%f %c %[^\n]s", &student[i].score,
                   &student[i].grade, student[i].name);
        }
        average = sum/num;
        fclose(file);
        printf("\n");
        goto Menu;
    }
    else if(menu == 8){
        printData(num, student);
        printf("\n");
        goto Menu;
    }
    else{
        printf("\nSee ya\n");
    }
    return 0;
}
