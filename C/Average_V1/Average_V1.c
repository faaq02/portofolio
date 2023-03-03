#include <stdio.h>

int main(){
   int num1, num2, num3, num4, num5;
   printf("Please enter first number :\n");
   scanf("%d", &num1);
   printf("Please enter second number :\n");
   scanf("%d", &num2);
   printf("Please enter third number :\n");
   scanf("%d", &num3);
   printf("Please enter fourth number :\n");
   scanf("%d", &num4);
   printf("Please enter fifth number :\n");
   scanf("%d", &num5);
   float total = (float)(num1 + num2 + num3 + num4 + num5) / 5;
   printf("%.2f\n", total);

   return 0;
}


