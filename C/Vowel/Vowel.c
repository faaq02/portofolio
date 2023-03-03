#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char text[1000], convert;
    int last = 0, vowel = 0, vowela = 0, voweli = 0,
    vowelu = 0, vowele = 0, vowelo = 0;
    program :
        printf("welcome to vowel finder\n");
        printf("enter your text :\n");
        printf("\n");
        scanf(" %[^\n]s", text);
        for(int i = 0; text[i] != '\0'; i++){
            if(text[i] == '\0'){
                break;
            }
            else{
                convert = text[i];
            }
            switch(convert){
            case 'a' : case 'A' : case 'i' :
            case 'I' : case 'u' : case 'U' :
            case 'e' : case 'E' : case 'o' :
            case 'O' : printf("v");
            break;
            case '.' : printf(".");
            break;
            case ',' : printf(",");
            break;
            case '/' : printf("/");
            break;
            case '"' : printf("\"");
            break;
            case '\'' : printf("'");
            break;
            case ':' : printf(":");
            break;
            case ' ' : printf(" ");
            break;
            default : printf("c");
            break;
            }
            if(text[i] == 'a' || text[i] == 'A' ||
               text[i] == 'i' || text[i] == 'I' ||
               text[i] == 'u' || text[i] == 'U' ||
               text[i] == 'e' || text[i] == 'E' ||
               text[i] == 'o' || text[i] == 'O'){
                last = 0;
               }
            else{
                last = 1;
            }
            switch(text[i]){
            case 'a' : case 'A' :
            ++vowel, ++vowela;
            break;
            case 'i' : case 'I' :
            ++vowel, ++voweli;
            break;
            case 'u' : case 'U' :
            ++vowel, ++vowelu;
            break;
            case 'e' : case 'E' :
            ++vowel, ++vowele;
            break;
            case 'o' : case 'O' :
            ++vowel, ++vowelo;
            break;
            }
        }
        if(last == 0){
            printf("\n");
            printf("\nends in vowel");
        }
        else{
            printf("\n");
            printf("\nends in consonant");
        }
        printf("\n");
        printf("\namount of vowel(s) : %d\n", vowel);
        printf("a : %d\n", vowela);
        printf("i : %d\n", voweli);
        printf("u : %d\n", vowelu);
        printf("e : %d\n", vowele);
        printf("o : %d\n", vowelo);
return 0;
}
