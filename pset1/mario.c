#include <stdio.h>
#include <cs50.h>
// This program prints mario's block when given an input of 1-23
 


int main(void)
{    
    int userInput;
    do
    { 
        printf("Height\n");

        userInput = get_int();
    }
    while(userInput < 0 &&userInput < 23);
    
    int hash = 1;
    int space = userInput - 1;
    
    for(int i = 0; i < userInput; i++)
    {
        
             for(int j= 1; j<= space; j++)
             {
                 printf(" ");
             }
             for(int k= 0; k< hash; k++)
             {
                 printf("#");
             }
             
             printf("\n");
             space--;
             hash ++;

    }
}
     





     
     
     
