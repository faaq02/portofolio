#include <stdio.h>

int main() {
    int i = 1, num, n;
    float total = 0, avg = 0;
    printf("hey gamer man, welcome to auto averager epicly\n");
    printf("how many numbers do you want gamer man?\n");
    scanf("%d", &n);
    printf("enter your number(s) gamer man\n");
    while (i <= n){
        printf("enter the epic number (%d/%d) :\n", i, n);
        scanf("%d", &num);
        i++;
        total = (total + num);
    }
    printf("the epic average is :%.2f\n", total / n);

    return 0;
}
