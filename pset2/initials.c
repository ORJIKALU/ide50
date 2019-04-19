#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
int main (void)
{
    printf("");
    string name;
    name = GetString();
    char initials[strlen(name)];
    initials[0] = name[0];
    int j = 0;
    j++;
    char currentChar;

    for (int i = 1; strlen(name) > i; i++)
    {
        currentChar = name[i];
        if (currentChar == ' ')
        {
            initials[j] = name[i+1];
            j++;
        }
    }
    for (int i = 0; i < j; i++)
    {
        printf("%c",toupper(initials[i]));
    }
    printf("\n");
}
