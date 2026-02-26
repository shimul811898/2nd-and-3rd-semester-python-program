#include <stdio.h>

int main() {
    int a, b;

    printf("Enter your value of a:");
    scanf("%d", &a);

    printf("Enter your value of b:");
    scanf("%d", &b);

    int addition=a+b;
    int subtraction=a-b;
    int multiplication=a*b;
    int division=a/b;
    int modules=a%b;

    printf("Your addition result is:%d \n",addition);
    printf("Your subtraction result is:%d \n",subtraction);
    printf("Your subtraction multiplication is:%d \n",multiplication);
    printf("Your division result is:%d \n",division);
    printf("Your modules result is:%d \n",modules);

    return 0;
}