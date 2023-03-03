#include <stdio.h>
#include <string.h>
#include <stdbool.h>

struct Student {
    char name[50];
    float score;
};

void inputStudent(int studentCount, struct Student *students){
    for(int i = 0; i < studentCount; i++){
            printf("Student #%d name : ", i + 1);
            scanf("%s", students[i].name);
            printf("Score : ", i + 1);
            scanf("%f", &students[i].score);
            while(students[i].score < 0 || students[i].score > 100){
                    printf("Value not valid, please re-enter : ", i + 1);
                    scanf("%f", &students[i].score);
        }
    }
}

void printAverageScore(int studentCount, struct Student *students){
    float average = 0;
    for(int i = 0; i < studentCount; i++){
            average += students[i].score;
    }
    average /= studentCount;
    printf("The average is : %.2f", average);
}

void swap(struct Student *a, struct Student *b){
    struct Student temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void printSortedScore(int studentCount, struct Student *students, bool isAscending){
    for(int i = 0; i < studentCount; i++){
            for(int j = 0; j < studentCount-i-1; j++){
                if(isAscending){
                    if(students[j].score > students[j+1].score){
                        swap(&students[j], &students[j+1]);
                }
            }
                else{
                    if(students[j].score < students[j+1].score) {
                        swap(&students[j], &students[j+1]);
                }
            }
        }
    }
    for(int i = 0; i < studentCount; i++){
        printf("\n%s\t:\t%.2f", students[i].name, students[i].score);
    }
}

void printMaxMinScore(int studentCount, struct Student *students){
    float max, min = students[0].score;
    for(int i = 0; i < studentCount; i++){
        if(students[i].score > max){
            max = students[i].score;
        }
        if(students[i].score < min){
            min = students[i].score;
        }
    }
    printf("\nThe max value is : %.2f", max);
    printf("\nThe min value is : %.2f", min);
}

void printMenu(){
    printf("\n\nWhat do you want to do? :");
    printf("\n1. Re-enter score");
    printf("\n2. Average the score");
    printf("\n3. Sort the score(Asc)");
    printf("\n4. Sort the score(Dsc)");
    printf("\n5. Find max and min of score");
    printf("\nOther number to quit : ");
}

int main() {
    int studentCount, inputMenu;

    input_student:
    printf("How many students do you have? : ");
    scanf("%d", &studentCount);
    struct Student students[studentCount];
    inputStudent(studentCount, students);

    menu:
    printMenu();
    scanf("%d", &inputMenu);
    switch (inputMenu) {
        case 1:
        goto input_student;
        case 2:
        printAverageScore(studentCount, students);
        goto menu;
        case 3:
        printSortedScore(studentCount, students, true);
        goto menu;
        case 4:
        printSortedScore(studentCount, students, false);
        goto menu;
        case 5:
        printMaxMinScore(studentCount, students);
        goto menu;
        default:
        printf("\nsee ya\n");
    }
    return 0;
}
