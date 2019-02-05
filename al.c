#include<stdio.h>
#include<conio.h>
int main(void)
{
char c;
printf("enter the character");
scanf("%c",&c);
if(c>='a' && c<='z')
{
printf("%c alphabet",c);
}
else
{
printf("%c not alphabet",c);
}
getch();
}
